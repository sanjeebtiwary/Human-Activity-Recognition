# Human-Activity-Recognition
Sure, here's an example description you could use for a GitHub repository on Human-Activity-Recognition:

# Human-Activity-Recognition

This project uses computer vision techniques and deep learning to recognize human activities in real-time. The application captures video frames from a webcam, and using a pre-trained convolutional neural network model, it predicts the activity being performed. The model has been trained on the Kinetics dataset, which contains over 400 human action classes.

## Usage

To use this application, simply run the `human_activity_recognition.py` script. Make sure you have the necessary dependencies installed, which can be found in the `requirements.txt` file. You will also need to download the pre-trained model and activity class labels, which can be found in the `models` folder.

When you run the script, your webcam will turn on and begin capturing frames. The application will predict the activity being performed in real-time, and display it on the screen.

## Dependencies

This project requires the following dependencies:

- Python 3.6 or higher
- OpenCV 4.5.3 or higher
- NumPy 1.20.3 or higher
- Onnxruntime 1.9.0 or higher

You can install all dependencies by running `pip install -r requirements.txt`.

Setup :
- I have added a video example for testing in `test` directory
- If you want to test your own video file be sure to add it in `test` folder
- Now, inside `recognise_human_activity.py` constructor set instance variable `VIDEO_PATH` to you file path.
- Otherwise, if you want test the model on using web-camera live video just set `self.VIDEO_PATH = None`
- Once your setup is done run the following to execute code:
- python recognise_human_activity.py

## Acknowledgments

This project was inspired by the work done in [this blog post](https://pyimagesearch.com/2019/11/25/human-activity-recognition-with-opencv-and-deep-learning/) by Adrian Rosebrock at PyImageSearch. The pre-trained model was trained by the authors of the Kinetics dataset, and can be found on their [GitHub repository](https://github.com/kenshohara/3D-ResNets-PyTorch).
