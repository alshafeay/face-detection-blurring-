# Real-Time Face Blurring & Detection

This project uses Python, OpenCV, and MediaPipe to perform real-time face detection and blurring on a live webcam feed. The primary purpose is to automatically anonymize faces for privacy. The script detects all faces in the frame, applies a strong blur effect to them, and draws a green bounding box around each one for clear visualization.



## Features
- **Live Face Detection:** Utilizes the high-performance MediaPipe Face Detection model to find faces in real-time.
- **Automatic Anonymization:** Applies a Gaussian blur effect to the detected facial regions automatically.
- **Visual Feedback:** Draws a rectangle around each detected face to show what is being anonymized.
- **Real-time Performance:** Processes the webcam feed with minimal latency.
- **Mirrored View:** Flips the camera feed horizontally for a more intuitive, mirror-like experience for the user.

## How It Works
The script follows these main steps for each frame captured from the webcam:

1.  **Capture Frame:** `OpenCV` is used to capture a frame from the default webcam.
2.  **Flip Frame:** The captured frame is flipped horizontally to create a "mirror view".
3.  **Color Conversion:** The frame, which is in BGR format by default in OpenCV, is converted to RGB format, as this is the format required by the MediaPipe library.
4.  **Face Detection:** The RGB frame is passed to the MediaPipe Face Detection model, which returns the locations of all detected faces.
5.  **Process Detections:**
    - For each detected face, the model provides a bounding box with relative coordinates (values between 0 and 1).
    - These relative coordinates are converted into absolute pixel coordinates based on the frame's width and height.
    - A specific region of interest (ROI) corresponding to the face's bounding box is selected from the original frame.
6.  **Apply Blur:** The `cv2.blur()` function from OpenCV is applied to this ROI, effectively anonymizing the face. The blurred ROI then replaces the original face region in the frame.
7.  **Draw Bounding Box:** A green rectangle is drawn around the blurred region using `cv2.rectangle()` to visually confirm the detection.
8.  **Display Output:** The final processed frame is displayed in a window titled 'Face Blur'.
9.  **Exit:** The application runs continuously until the user presses the `ESC` key.



2.  **Install the required packages:**
    You can install all necessary libraries using pip. It's recommended to do this in a virtual environment.
    ```bash
    pip install opencv-python mediapipe numpy
    ```

## Usage
To run the face blurring application, simply execute the `main.py` script from your terminal:
```bash
python main.py
```
- A window will appear showing your webcam feed.
- Any faces detected by the camera will be automatically blurred.
- To stop the program, press the `ESC` key while the output window is active.

## Acknowledgments
- This project relies on the powerful and efficient [MediaPipe](https://google.github.io/mediapipe/) library by Google for face detection.
- All video capture and image processing functionalities are handled by the [OpenCV](https://opencv.org/) library.
