import cv2
import mediapipe as mp
import socket

# Initialize MediaPipe Hand Module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Connect to Raspberry Pi Pico WH via Wi-Fi
SERVER_IP = "192.168.137.192"  # Replace with your Pico WH IP
SERVER_PORT = 5000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER_IP, SERVER_PORT))

# Open Camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Flip for better experience
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    finger_count = 0

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            finger_tips = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky
            finger_up = []

            for tip in finger_tips:
                if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
                    finger_up.append(1)  # Finger is up
                else:
                    finger_up.append(0)  # Finger is down

            finger_count = sum(finger_up)  # Count fingers

            # Send data to Raspberry Pi Pico WH
            if finger_count == 5:
                sock.sendall(b'ON')  # Light ON
            elif finger_count == 0:
                sock.sendall(b'OFF')  # Light OFF

    cv2.putText(frame, f"Fingers: {finger_count}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Hand Gesture Controller", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

sock.close()
cap.release()
cv2.destroyAllWindows()
