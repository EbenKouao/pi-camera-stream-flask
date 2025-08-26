import io
import time
import logging
from threading import Condition
from picamera2 import Picamera2
from picamera2.encoders import JpegEncoder
from picamera2.outputs import FileOutput

# Set up logging
logging.basicConfig(level=logging.INFO)


class StreamingOutput(io.BufferedIOBase):
    """
    A thread-safe, in-memory stream for the camera's JPEG output.
    """

    def __init__(self):
        self.frame = None
        self.condition = Condition()

    def write(self, buf: bytes) -> int:
        """
        Called by the encoder. Writes the frame to the buffer and notifies
        any waiting threads.
        :param buf: The buffer containing the JPEG frame.
        :type buf: bytes
        """
        with self.condition:
            self.frame = buf
            self.condition.notify_all()
        return len(buf)


class VideoCamera(object):
    """
    A class that manages the Raspberry Pi camera using picamera2 for
    efficient, hardware-accelerated MJPEG streaming.
    """

    def __init__(self, flip: bool = False):
        """
        Initializes the camera, configures it for streaming, and starts
        the hardware encoder.

        :param flip: Whether to flip the camera feed vertically and horizontally.
        :type flip: bool
        """
        logging.info("Initializing camera...")
        self.picam2 = Picamera2()

        # --- Streaming Configuration ---
        # Reduced resolution for smoother web streaming and lower latency.
        # The hardware encoder works with YUV420 format.
        video_config = self.picam2.create_video_configuration(
            main={"size": (1280, 720), "format": "YUV420"},
            controls={"FrameRate": 30}
        )
        self.picam2.configure(video_config)

        # --- Still Image Configuration ---
        # A separate, higher-resolution configuration for taking still photos.
        self.still_config = self.picam2.create_still_configuration()

        # Set flip controls if needed
        if flip:
            self.picam2.set_controls({"VFlip": True, "HFlip": True})

        self.output = StreamingOutput()
        self.encoder = JpegEncoder()

        # Start the encoder in a background thread
        self.picam2.start_recording(self.encoder, FileOutput(self.output))

        logging.info("Camera initialized and recording started.")
        time.sleep(1)  # Allow camera to warm up

    def __del__(self):
        """
        Stops the recording thread when the object is destroyed.
        """
        logging.info("Stopping camera recording.")
        self.picam2.stop_recording()

    def get_frame(self) -> bytes:
        """
        Waits for a new frame from the encoder and returns it.

        :return: A complete JPEG frame as a byte string.
        :rtype: bytes
        """
        with self.output.condition:
            self.output.condition.wait()
            frame = self.output.frame
        return frame

    def take_picture(self):
        """
        Temporarily stops the stream, switches to high-resolution config,
        takes a photo, and then restarts the stream.
        """
        logging.info("Stopping recording to capture a still image.")
        self.picam2.stop_recording()
        time.sleep(0.5)  # Allow time for the encoder to stop

        try:
            # Switch to still configuration and capture
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            filename = f"stream_photo_{timestamp}.jpg"
            logging.info(f"Capturing still image to {filename}...")
            self.picam2.switch_mode_and_capture_file(self.still_config, filename)
            logging.info("Still image captured.")
        finally:
            # Ensure the stream is restarted
            logging.info("Restarting video stream recording.")
            self.picam2.start_recording(self.encoder, FileOutput(self.output))

