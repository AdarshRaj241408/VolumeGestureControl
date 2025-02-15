# Hand Tracking Volume Control

## Overview
This project implements a **hand tracking-based volume control system** using **OpenCV**, **MediaPipe**, and **PulseAudio** (for Linux). The application detects hand gestures and adjusts the system volume based on the distance between the thumb and index finger.

## Features
- **Hand Tracking with MediaPipe**: Uses Google's **MediaPipe** library to detect and track hand landmarks.
- **Gesture-Based Volume Control**: The distance between the thumb and index finger controls the volume.
- **Cross-Platform Support**:
  - Uses `pycaw` for Windows (commented out in the code).
  - Uses `pulsectl` for Linux to adjust volume via PulseAudio.
- **Real-Time FPS Display**: Shows the frame rate (FPS) for performance monitoring.

## Dependencies
Make sure you have the following Python libraries installed:
```sh
pip install opencv-python mediapipe numpy pulsectl
```
For Windows, you may need:
```sh
pip install pycaw comtypes
```

## File Structure
```
📂 HandTrackingVolumeControl
 ├── HandTrackingModule.py   # Hand tracking helper module
 ├── VolumeHandControl.py    # Main script for volume control
 ├── README.md               # Project documentation
```

## Usage
Run the volume control script:
```sh
python VolumeHandControl.py
```

## How It Works
1. **Hand Detection**: Uses **MediaPipe Hands** to track the hand in real time.
2. **Landmark Extraction**: Extracts the positions of the thumb and index finger.
3. **Volume Mapping**: Maps the distance between these fingers to a volume range (0-100%).
4. **System Volume Adjustment**:
   - On **Linux**, it uses `pulsectl` to set the system volume.
   - On **Windows**, `pycaw` (commented in code) can be used instead.
5. **Visual Feedback**:
   - Displays a **volume bar** on the screen.
   - Highlights the detected hand landmarks and gestures.

## Example Output
- When fingers are **close together** → **Lower Volume**
- When fingers are **far apart** → **Increase Volume**
- If fingers are very close, the circle turns **green** (visual confirmation)

## Future Improvements
- Add Windows compatibility with `pycaw`.
- Implement smooth volume transitions.
- Support multiple hand gestures for different actions.

## Author
Developed by **Adarsh Raj**

---
🚀 **Happy Coding!**