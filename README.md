# YOLO Webcam Rock-Paper-Scissors Detection

A beginner-friendly computer vision project that detects objects in real time using a webcam. Built with Python, OpenCV, and the Ultralytics YOLO framework.

## Features

- Real-time object detection through a webcam
- Bounding boxes around detected objects
- Object class labels
- Confidence scores for predictions
- Adjustable confidence threshold
- Press `q` to close the webcam window

## Technologies Used

- Python
- OpenCV
- Ultralytics YOLO
- PyTorch (used by the Ultralytics framework)

## Project Structure

```text
yolo-webcam-object-detection/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
├── best.pt
└── assets/
    └── demo.png
```

The `best.pt` file is a trained model checkpoint required by the current code. The `assets/` folder is optional and can contain screenshots of the output.

## Requirements

- Python 3.10 or another Python version supported by your installed Ultralytics release
- A working webcam
- pip
- A compatible PyTorch and Ultralytics installation
- The `best.pt` model file

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/yolo-webcam-object-detection.git
cd yolo-webcam-object-detection
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add the model file

Place your trained `best.pt` file in the root project folder, alongside `main.py`.

Make sure the model file is compatible with the installed Ultralytics version.

### 5. Run the project

```bash
python main.py
```

A webcam window should open and display detected objects with bounding boxes, labels, and confidence scores.

Press `q` while the video window is active to exit.

## Configuration

The current detection confidence threshold is set to `0.5`:

```python
results = model(frame, conf=0.5)
```

Increase the value to make detection more selective, or decrease it to allow more detections. Actual performance depends on the model and video conditions.

## Troubleshooting

- **Could not open the webcam:** Check webcam permissions and close other applications using the camera. Try changing `cv2.VideoCapture(0)` to `cv2.VideoCapture(1)` if another camera is available.
- **`best.pt` not found:** Ensure the model file is in the same directory as `main.py`.
- **Missing module errors:** Activate your virtual environment and install the dependencies.
- **Slow detection:** Try a smaller model or a system with suitable GPU support.
- **No detections:** Verify that the model is trained for the objects you expect to detect.

## Learning Objectives

This project demonstrates how to load a trained object detection model, capture webcam frames, run inference, visualize predictions, and release camera resources safely.

## Disclaimer

This project is intended for educational and demonstration purposes. Detection accuracy depends on the model, training data, lighting, camera quality, and environment.

## License

Add a license if you want others to reuse or distribute your code. Check the model's origin and applicable license before redistributing `best.pt`.
