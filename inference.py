import tensorflow as tf
import numpy as np
import json
import requests
import tensorflow_datasets as tfds


# Define a function which takes an integer representing a class in the dataset and returns the name of the class.
def format_label(label):
    # Get the name of the class representing the passed index.
    string_label = label_info.int2str(label)
    # Clean up the string to get only the name of the dog breed.
    string_label = string_label.split("-")[1].replace("_", " ")
    # Capitalise the string and return it.
    return string_label.title()


# Define the required image size for the model input.
SIZE = 300
# Define the URI for making prediction requests to the TensorFlow model which is being served.
MODEL_URI = 'http://localhost:8501/v1/models/DogModel:predict'
# Define a TensorFlow dataset builder for the dataset used to train the model.
builder = tfds.builder('stanford_dogs')
# Extract the metadata for that dataset.
info = builder.info
# Get all the possible labels (classes) that the model can predict.
label_info = info.features["label"]


# Define a function for making predictions, which takes a path to an image as an input argument.
def get_prediction(image_path):
    # Read the image and resize it.
    image = tf.keras.preprocessing.image.load_img(
        image_path, target_size=(SIZE, SIZE))
    # Convert the image to a numpy array.
    image = tf.keras.preprocessing.image.img_to_array(image)
    # Add a dimension at axis 0 to make the image match the expected input shape by the model.
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
    # Get the result value for key 'predictions' and remove any extra dimensions, giving a probability for each class.
    prediction = np.squeeze(result['predictions'][0])
    # Get the index for the class with the highest probability
    # and pass it to the format_label function to get a class name.
    class_name = format_label(np.argmax(prediction))
    # Return the predicted class name.
    return class_name
