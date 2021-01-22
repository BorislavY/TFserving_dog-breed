# TFserving_dog-breed
Deploying a dog breed detector with TensorFlow Serving and Flask

This project was built following the instructions 
[in this guide](https://www.coursera.org/projects/deploy-models-tensorflow-serving-flask),
and then modified to work with an EfficientNet-B3 (Noisy Student) model trained on the
Stanford Dogs dataset.
Detailed comments were added to show understanding of the code.

## Setting up TensorFlow Serving with Docker
**To set up a Docker container:**

Replace \<ABSOLUTE PATH\> with your absolute path to the "DogModel" folder.
```console
$ sudo docker run -p 8501:8501 --name=DogModel -v "<ABSOLUTE PATH>:/models/DogModel/1" -e MODEL_NAME=DogModel tensorflow/serving
```
**After creating the container once, it can be run in the future with:**
```console
$ sudo docker start DogModel
```

## Demonstration
Start the container and run **app.py** to start the Flask web application.

Open the application by going to [localhost port 5000](http://127.0.0.1:5000/).

Choose a file and upload it to get a prediction:

![This GIF died :(](https://media.giphy.com/media/gS6tCLbeipyvyjjead/giphy.gif)

