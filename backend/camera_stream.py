import cv2 as cv
import mediapipe as mp

from backend.hand_landmarker import create_hand_landmarker
from backend.gesture_rules import detect_gesture
from backend.drawing_utils import draw_text, draw_landmarks

#--------- Create Hand Landmark once ---------

landmarker = create_hand_landmarker()

#--------- Timestamp for video mode ----------
timestamp = 0
current_sign = "UNKNOWN"
stable_count = 0

STABLE_FRAMES = 10

def process_frame(frame):

    global timestamp
    global current_sign
    global stable_count

    # Convert BGR to RGB
    rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    # Create MediaPipe image
    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb
    )

    # Detect hand landmarks
    results = landmarker.detect_for_video(
        mp_image,
        timestamp
    )

    # Increment timestamp
    timestamp += 33

    # If hand detected
    if results.hand_landmarks:

        # Draw skeleton
        frame = draw_landmarks(
            frame,
            results.hand_landmarks
        )

        # Use the first hand
        hand = results.hand_landmarks[0]

        # Detect gesture
        sign = detect_gesture(hand)

        # Draw gesture name
        frame = draw_text(
            frame,
            sign
        )

        from backend.speaker import speak

        # Stabilize gesture
        if sign == current_sign:
            stable_count += 1
        else:
            current_sign = sign
            stable_count = 1

        if stable_count == STABLE_FRAMES:
            speak(sign)
    else:
        current_sign = "UNKNOWN"
        stable_count = 0

    return frame