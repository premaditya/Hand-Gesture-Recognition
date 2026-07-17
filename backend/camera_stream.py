import cv2 as cv
import mediapipe as mp

from backend.hand_landmarker import create_hand_landmarker
from backend.gesture_rules import detect_gesture
from backend.drawing_utils import draw_text, draw_landmarks
from backend.speaker import speak

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

    print("Frame Received")

    # Convert BGR to RGB
    rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    # Create MediaPipe image
    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb
    )

    print("Running MediaPipe Detection")

    # Detect hand landmarks
    results = landmarker.detect_for_video(
        mp_image,
        timestamp
    )

    # Increment timestamp
    timestamp += 33

    # If hand detected
    if results.hand_landmarks:
        print("Hand Detected")

        print("Drawing Landmarks")
        frame = draw_landmarks(
            frame,
            results.hand_landmarks
        )

        print("Getting First Hand")
        hand = results.hand_landmarks[0]

        print("Detecting Gesture")
        sign = detect_gesture(hand)
        print(f"Detected Gesture: {sign}")

        print("Drawing Text")
        frame = draw_text(
            frame,
            sign
        )

        

        print("Checking Stability")

        # Stabilize gesture
        if sign == current_sign:
            stable_count += 1
        else:
            current_sign = sign
            stable_count = 1

        print(f"Stable Count: {stable_count}")

        if stable_count == STABLE_FRAMES:
            print("Calling speak()")
            speak(sign)
            print("speak() Finished")

    else:
        print("No Hand Detected")
        current_sign = "UNKNOWN"
        stable_count = 0

    print("Returning Frame\n")

    return frame