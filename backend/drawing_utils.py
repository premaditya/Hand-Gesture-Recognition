import cv2 as cv

#----- Hand Connections (21 Landmarks) ----------

HAND_CONNECTIONS = [
    (0,1), (1,2), (2,3), (3,4),
    (0,5), (5,6), (6,7), (7,8),
    (5,9), (9,10), (10,11), (11,12),
    (9,13), (13,14), (14,15), (15,16),
    (13,17), (17,18), (18,19), (19,20),
    (0,17)
]

def draw_text(frame, text):
    cv.putText(
        frame,
        text,
        (20,50),
        cv.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
    )

    return frame

def draw_landmarks(frame, hand_landmarks):

    h, w, _ = frame.shape

    for hand in hand_landmarks:

        points =[]

        # Draw landmarks points
        for lm in hand:
            x = int(lm.x * w)
            y = int(lm.y * h)

            points.append((x,y))

            cv.circle(
                frame,
                (x,y),
                5,
                (0,255,0),
                -1
            )

        # Draw connection
        for start,end in HAND_CONNECTIONS:

            cv.line(
                frame,
                points[start],
                points[end],
                (255,0,0),
                2
            )
    
    return frame