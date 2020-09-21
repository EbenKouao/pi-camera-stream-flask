# Make you own Raspberry Pi Camera Stream

Create your own live stream from a Raspberry Pi using the Pi camera module. Build your own applications from here.

## How it works
The Pi streams the output of the camera module over the web via Flask. Devices connected to the same network would be able to access the camera stream via

```
<raspberry_pi_ip:5000> 
```

## Screenshots
| ![Setup](img/readme/[].png) | ![Live Pi Camera Stream](img/readme/[].png) |
|---|---|
| Pi Setup | Pi - Live Stream |

## Preconditions

* Raspberry Pi 4, 2GB is recommended for optimal performance. However you can use a Pi 3 or older, you may see a increase in latency.
* Raspberry Pi 4 Camera Module or Pi HQ Camera Module (Newer version)
* Python 3 recommended.

## Step 1 – Cloning Raspberry Pi Camera Stream
Open up terminal and clone the Camera Stream repo:

```
bash cd /home/pi
git clone []
```

## Step 2 – Launch Web Stream

Note: Creating an Autostart of the main.py script is recommended to keep the stream running on bootup.
```bash cd modules
sudo python3 /home/pi/[]/main.py
```
## Download Beta image of Raspberry Pi Camera Stream
Any troubles installing, try out the already compiled Raspberry Pi (Raspbian OS) Image of [Raspberry Pi Camera Stream](https://smartbuilds.io).
![Raspbian Camera Stream Image](img/readme/[].png)
