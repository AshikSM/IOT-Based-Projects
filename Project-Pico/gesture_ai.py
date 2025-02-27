import cv2
import mediapipe as mp
import socket

# Pico W IP and port
PICO_IP = "192.168.137.45"  # Replace with your Pico's IP
PICO_PORT = 80

# Initialize Mediapipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Initialize webcam
cap = cv2.VideoCapture(0)

# Socket setup
def send_command(command):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((PICO_IP, PICO_PORT))
        sock.send(command.encode())
        print(f"Sent: {command}")
        sock.close()
    except Exception as e:
        print(f"Error sending command: {e}")

last_state = None

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip and convert frame to RGB
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process frame with Mediapipe
    result = hands.process(rgb_frame)
    finger_count = 0

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:

            # Draw hand landmarks
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Count fingers (simple heuristic: check if fingertips are above wrist)
            landmarks = hand_landmarks.landmark
            wrist_y = landmarks[0].y  # Wrist landmark
            finger_tips = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky
            finger_count = sum(1 for tip in finger_tips if landmarks[tip].y < wrist_y)

    # Send command based on finger count
    if finger_count == 5 and last_state != "ON":
        send_command("ON")
        last_state = "ON"
    elif finger_count == 0 and last_state != "OFF":
        send_command("OFF")
        last_state = "OFF"

    # Display finger count
    cv2.putText(frame, f"Fingers: {finger_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Gesture Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()