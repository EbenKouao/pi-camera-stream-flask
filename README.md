# Make you own Raspberry Pi Camera Stream

Create your own live stream from a Raspberry Pi using the Pi camera module. Build your own applications from here.

## How it works
The Pi streams the output of the camera module over the web via Flask. Devices connected to the same network would be able to access the camera stream via

```
<raspberry_pi_ip:5000>
```

## Screenshots
| ![Setup](readme/pi-stream-client.jpg) | ![Live Pi Camera Stream](readme/pi-stream-screen-capture.jpg) |
| ------------------------------------- | ------------------------------------------------------------- |
| Pi Setup                              | Pi - Live Stream                                              |

## Preconditions

* Raspberry Pi 4, 2GB is recommended for optimal performance. However you can use a Pi 3 or older, you may see a increase in latency.
* Raspberry Pi 4 Camera Module or Pi HQ Camera Module (Newer version)
* Python 3 recommended.

## Library dependencies
Make your Raspberry Pi is up to date and has the required libraries installed. 
```bash
sudo apt-get update
sudo apt-get upgrade
```
Install the following dependencies to create camera stream.

```bash
sudo apt-get install libatlas-base-dev libjasper-dev libqtgui4 libqt4-test libhdf5-dev python3-picamera2
```
Then install openCV
```bash
sudo apt install build-essential cmake git libgtk-3-dev libavcodec-dev libavformat-dev libswscale-dev
```

Note: This installation of opencv may take a while depending on your pi model.

OpenCV alternate installation (in the event of failed opencv builds):

```bash
sudo apt-get install libopencv-dev python3-opencv
```

## Step 1 – Cloning Raspberry Pi Camera Stream
Open up terminal and clone the Camera Stream repo:

```bash
cd /home/pi
git clone https://github.com/EbenKouao/pi-camera-stream-flask.git
```

## Step 2 - make virtual environment (optional)
I like to use a virtual environment for my projects, so I can keep the dependencies separate. You can skip this step if 
you do not want to use a virtual environment.

```bash
cd /home/pi/pi-camera-stream-flask
python3 -m venv --system-site-packages venv
```
`--system-site-packages` allows the virtual environment to access the system's site-packages directory, such as OpenCV 
and picamera2.
```bash
source venv/bin/activate
```
## Step 3 – Install dependencies
```bash
cd /home/pi/pi-camera-stream-flask
pip install -r requirements.txt
```
or if you are not using the virtual environment:
```bash
sudo python3 -m pip install -r requirements.txt
```
## Step 4 – Launch Web Stream

Note: Creating an Autostart of the main.py script is recommended to keep the stream running on bootup.
```bash 
sudo python3 /home/pi/pi-camera-stream-flask/main.py
```

## Step 5 – Autostart your Pi Stream (Optional)

Optional: A good idea is to make the camera stream auto start at bootup of your pi. You can add a systemd service to do this.

If you do not use a virtual environment or installed the project outside of `/home/pi`, you will have to modify `launch_service.sh`.
### 5.1 - Make the launcher script executable
```bash
chmod +x /home/pi/pi-camera-stream-flask/launch_service.sh
```
### 5.2 - Create a systemd service
```bash
sudo nano /etc/systemd/system/pi-camera-stream.service
```
paste the following content into the file:
```ini
[Unit]
Description=My Python Startup Script
After=network.target

[Service]
User=pi
WorkingDirectory=/home/pi/pi-camera-stream-flask
ExecStart=/home/pi/pi-camera-stream-flask/launch_service.sh
Restart=always

[Install]
WantedBy=multi-user.target
```
save and exit the file (Ctrl + X, then Y, then Enter).
### 5.3 - Enable and start the service
```bash
sudo systemctl daemon-reload
sudo systemctl enable pi-camera-stream.service
sudo systemctl start pi-camera-stream.service
```
You can check the status of the service with:
```bash
sudo systemctl status pi-camera-stream.service
```
If everything is working, you should see a green "active (running)" message. Using services allows you to manage the 
camera stream easily, start on startup (if network is available) and restart the service if it fails.
## More Projects / Next Steps
View the latest Build: [Pi Smart Cam with Motion Sensor](https://github.com/EbenKouao/pi-smart-cam)

Alternatively, view more projects that build on the Pi Camera on [smartbuilds.io](https://smartbuilds.io).

