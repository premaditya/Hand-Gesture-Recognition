# ✋ Hand Gesture Recognition using MediaPipe

A real-time hand gesture recognition application built using **Python, OpenCV, and MediaPipe**.

This project recognizes predefined hand gestures using rule-based logic instead of machine learning. MediaPipe detects 21 hand landmarks, and the application compares the positions of fingertips and finger joints to determine whether each finger is open or folded. Based on these finger states, predefined gesture rules are used to recognize different hand gestures.

The detected gesture is displayed on the screen and spoken aloud using **Microsoft Edge Text-to-Speech (edge-tts)**.

---

## Features

- Real-time webcam detection
- MediaPipe hand tracking
- Rule-based gesture recognition
- Voice output using Edge TTS
- Live prediction display

---

## Technologies Used

- Python
- OpenCV
- MediaPipe
- edge-tts
- playsound
- asyncio

---

## Project Structure

```
Hand_Gesture_Recognition/
│
├── backend/
│
├── Models/
│
├── app.py
├── requirements.txt
```

---

## Installation

Clone the repository

```bash
git clone <YOUR_GITHUB_REPO_LINK>
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
python app.py
```

---

## How It Works

- The webcam captures live video.
- MediaPipe detects 21 hand landmarks.
- Finger positions are calculated using fingertip and joint landmarks.
- A set of predefined gesture rules determines which hand gesture is being shown.
- The detected gesture is displayed on the screen.
- The detected gesture is spoken using Microsoft Edge Text-to-Speech (edge-tts).

**This project uses rule-based gesture recognition and does not use a machine learning model.**

---

## Future Improvements

- Support dynamic gestures
- Add more hand signs
- Improve recognition under different lighting conditions
- Sentence formation from multiple signs

---

## Demo

A demo video is available in my LinkedIn post.

---

## Author

Prem Aditya