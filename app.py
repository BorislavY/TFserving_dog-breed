from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap
import os
import inference

# Initialise the Flask application
app = Flask(__name__)
# Add Bootstrap functionality to the app by passing it through the Bootstrap class.
Bootstrap(app)


# Define routes for GET and POST requests made to the main page of the Flask app.
@app.route('/', methods=['GET', 'POST'])
def index():
    # For a POST request, execute this code to infer a result.
    if request.method == 'POST':
        # Get the file uploaded in the form.
        uploaded_file = request.files['file']
        # If there is an uploaded file execute this code.
        if uploaded_file.filename != '':
            # Define a path for saving this image in the "static" folder.
            image_path = os.path.join('static', uploaded_file.filename)
            # Save the uploaded image to display it later.
            uploaded_file.save(image_path)
            # Get a class name by making a prediction on the image.
            class_name = inference.get_prediction(image_path)
            # Print the class name in the terminal.
            print('CLASS NAME = ', class_name)
            # Define an object/dictionary to store the class name and path to the saved image.
            result = {
                'class_name': class_name,
                'image_path': image_path
            }
            # Pass the result to show.html and render the page.
            return render_template('show.html', result=result)
    # For a GET request, render index.html
    return render_template('index.html')


# If this scrip is executed, run the application with debugging engaged.
if __name__ == '__main__':
    app.run(debug=True)
