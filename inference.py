import tensorflow as tf
import numpy as np
import json
import requests

# Define the required image size for the model input.
SIZE = 128
# Define the URI for making prediction requests to the TensorFlow model which is being served.
MODEL_URI = 'http://localhost:8501/v1/models/pets:predict'
# Define the two possible output classes.
CLASSES = ['Cat', 'Dog']


# Define a function for making predictions, which takes a path to an image as an input argument.
def get_prediction(image_path):
    # Read the image and resize it.
    image = tf.keras.preprocessing.image.load_img(
        image_path, target_size=(SIZE, SIZE))
    # Convert the image to a numpy array.
    image = tf.keras.preprocessing.image.img_to_array(image)
    # Apply the same normalization which was used when training the model.
    image = tf.keras.applications.mobilenet_v2.preprocess_input(image)
    # Add a dimension at axis 0 to make the image match the expected input shape for the model.
    image = np.expand_dims(image, axis=0)

    # Encode the data as a JSON string.
    data = json.dumps({
        # TensorFlow serving requires the data to be encoded as a list with key 'instances'
        'instances': image.tolist()
    })
    # Encode the string to UTF-8 (default) as required for TensorFlow serving, and make a post request to the URI.
    response = requests.post(MODEL_URI, data=data.encode())

    # Decode the response of the model as a dictionary.
    result = json.loads(response.text)
    # Get the result value for key 'predictions' and remove any extra dimensions, giving a class probability.
    prediction = np.squeeze(result['predictions'][0])
    # Translate the probability into one of the two possible classes.
    class_name = CLASSES[int(prediction > 0.5)]
    # Return the predicted class name.
    return class_name
