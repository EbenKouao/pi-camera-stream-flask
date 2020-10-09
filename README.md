# Make you own Raspberry Pi Camera Stream

Create your own live stream from a Raspberry Pi using the Pi camera module. Build your own applications from here.

## How it works
The Pi streams the output of the camera module over the web via Flask. Devices connected to the same network would be able to access the camera stream via

```
<raspberry_pi_ip:5000> 
```

## Screenshots
| ![Setup](readme/pi-stream-client.jpg) | ![Live Pi Camera Stream](readme/pi-stream-screen-capture.jpg) |
|---|---|
| Pi Setup | Pi - Live Stream |

## Preconditions

* Raspberry Pi 4, 2GB is recommended for optimal performance. However you can use a Pi 3 or older, you may see a increase in latency.
* Raspberry Pi 4 Camera Module or Pi HQ Camera Module (Newer version)
* Python 3 recommended.

## Library dependencies
Install the following dependencies to create camera stream.

```
bash sudo apt-get update 
sudo apt-get upgrade
sudo apt-get install libatlas-base-dev
sudo apt-get install libjasper-dev
sudo apt-get install libqtgui4 
sudo apt-get install libqt4-test
sudo apt-get install libhdf5-dev
pip3 install flask
pip3 install numpy
pip3 install opencv-contrib-python
pip3 install imutils
```

pip3 install opencv-python

## Step 1 – Cloning Raspberry Pi Camera Stream
Open up terminal and clone the Camera Stream repo:

```
bash cd /home/pi
git clone https://github.com/EbenKouao/pi-camera-stream-flask.git
```

## Step 2 – Launch Web Stream

Note: Creating an Autostart of the main.py script is recommended to keep the stream running on bootup.
```bash cd modules
sudo python3 /home/pi/[]/main.py
```
## Download Beta image of Raspberry Pi Camera Stream
Any troubles installing, try out the already compiled Raspberry Pi (Raspbian OS) Image of [Raspberry Pi Camera Stream](https://smartbuilds.io).
![Raspbian Camera Stream Image](img/readme/[].png)
