#Modified by smartbuilds.io
#Date: 27.09.20
#Desc: This web application serves a motion JPEG stream
# main.py
# import the necessary packages
from flask import Flask, render_template, Response, request, send_from_directory
from camera import VideoCamera
import os

framerate = None
pi_camera = None

# App Globals (do not edit)
app = Flask(__name__)

def formatFrame(frame):
    return (b'--frame.jpg\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/')
def index():
    return render_template('index.html') #you can customze index.html here

def gen(camera):
    #get camera frame
    while True:
        frame = camera.get_frame()
        res = formatFrame(frame)
        yield res

@app.route('/video_feed')
def video_feed():
    return Response(gen(pi_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# Take a photo when pressing camera button
@app.route('/picture')
def take_picture():
    from io import BytesIO
    from PIL import Image
    #pi_camera.take_picture()
    frame = pi_camera.get_frame()
    image = Image.open(io.BytesIO(frame))
    
    frame = BytesIO()
    image.save(frame, 'JPEG', quality=100)
    frame.seek(0)
    return send_file(frame, mimetype='image/jpeg')

# Get a single frame
@app.route('/frame')
def get_frame():
    import io
    from io import BytesIO
    from PIL import Image
    from flask import send_file

    frame = pi_camera.get_frame()
    # res = formatFrame(frame)
    # return Response(res,
    #                 mimetype='multipart/x-mixed-replace; boundary=frame')
    # old code:
    image = Image.open(io.BytesIO(frame))
    
    frame = BytesIO()
    image.save(frame, 'JPEG', quality=100)
    frame.seek(0)
    return send_file(frame, mimetype='image/jpeg')
    
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Webcam demo')
    parser.add_argument('--framerate', required=True, default=2 ,help='Set framerate of the camera')
    framerate = parser.parse_args().framerate
    pi_camera = VideoCamera(flip=False, framerate=framerate) # flip pi camera if upside down.


    app.run(host='0.0.0.0', debug=False, port=5001)
