# 🕹️ Gesture-Based Game Controller 

This is a Gesture-Based Game Controller that allows you to play games like Dr. Driving using only your hand gestures—no physical keyboard required!

By simply showing your hand to your webcam, the system can detect:

- How many fingers you're holding up

- Whether your hand is tilted left, right, or centered

- These gestures are then translated into keyboard controls using simulated key presses.
---
## 🔍 How It Works
This project brings together powerful libraries to deliver real-time gesture control:

- MediaPipe: For detecting and tracking hand landmarks with high accuracy
- OpenCV: For handling live video capture and visual overlays
- PyAutoGUI: To simulate keyboard inputs so you can control your game with gestures
## 🚗 Features

-  **Hand Gesture Recognition** via webcam
- Simulated keyboard controls for:
  - Accelerate (`W`) with 4+ fingers up
  - Brake (`S`) with fist or 1 finger
  - Turn Left (`A`) or Right (`D`) by hand tilt
- Real-time video overlay with:
  - Landmarks
  - Fingertip coordinates
  - Gesture status (`Accelerating`, `Braking`, etc.)

---
## 🎮 Game Controls Logic

| Gesture                        | Action        | Key Press |
|-------------------------------|---------------|-----------|
| 4 or more fingers up          | Accelerate    | `W`       |
| Fist or only 1 finger up      | Brake         | `S`       |
| Hand tilted left (x > +200)   | Turn Left     | `A`       |
| Hand tilted right (x < -200)  | Turn Right    | `D`       |
| Neutral                       | Release keys  | `-`       |

## 🛠 Requirements

- Python 3.7+
- Webcam
  
## 📸 Setup Instructions

1. **Clone this repository** or download the script:

```bash
git clone https://github.com/your-username/gesture-driving-control.git
cd gesture-driving-control
```
2. Install the required Python packages:

```bash
pip install -r requirements.txt
```
  
3. Run the python file

```bash
python run gesture_controller.py
```
4. Start the Dr. Driving game on your respective device and wait for the webcam to initiate before pressing PLAY. Once the webcam starts, click on PLAY and Enjoy :)

