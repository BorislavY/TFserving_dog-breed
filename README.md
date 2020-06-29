# TFserving_cat-dog
Deploying a cat-dog detector with TensorFlow Serving and Flask

This project was built following the instructions 
[in this guide.](https://www.coursera.org/projects/deploy-models-tensorflow-serving-flask)
Detailed comments were added to show understanding of the code. An already trained machine
learning model was used for the task.

## Setting up TensorFlow Serving with Docker
**To set up a Docker container:**

Replace \<ABSOLUTE PATH\> with your absolute path to the "pets" folder.
```console
$ sudo docker run -p 8501:8501 --name=pets -v "<ABSOLUTE PATH>:/models/pets/1" -e MODEL_NAME=pets tensorflow/serving
```
**After creating the container once, it can be run in the future with:**
```console
$ sudo docker start pets
```

## Demonstration
Start the container and run **app.py** to start the Flask web application.

Open the application by going to [localhost port 5000](http://127.0.0.1:5000/).

Choose a file and upload it to get a prediction:

![This GIF died :(](https://media.giphy.com/media/XCyl3Ik6GDxMiXSHEL/source.gif)

