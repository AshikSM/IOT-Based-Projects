import cv2
import mediapipe as mp
import serial
import time

# Initialize Serial Communication (Adjust COM Port)
SERIAL_PORT = "COM4"  # Change to /dev/ttyUSB0 for Linux
ser = serial.Serial(SERIAL_PORT, 115200, timeout=1)

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# Open Camera
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        continue

    # Convert to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process hand tracking
    results = hands.process(rgb_frame)

    finger_count = 0  # Default: No fingers detected

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Finger landmark indices (Tips)
            finger_tips = [8, 12, 16, 20]  # Index, Middle, Ring, Pinky
            thumb_tip = 4

            # Get landmarks
            landmarks = hand_landmarks.landmark

            # Count extended fingers
            for tip in finger_tips:
                if landmarks[tip].y < landmarks[tip - 2].y:  # Tip above knuckle
                    finger_count += 1

            # Thumb check
            if landmarks[thumb_tip].x > landmarks[thumb_tip - 1].x:  # Thumb outward
                finger_count += 1

    # Display Finger Count
    cv2.putText(frame, f'Fingers: {finger_count}', (50, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Send Data to Pico WH
    if finger_count == 5:
        ser.write(b'ON\n')  # Send "ON" to Pico WH
    elif finger_count == 0:
        ser.write(b'OFF\n')  # Send "OFF" to Pico WH

    # Show Camera Output
    cv2.imshow("Gesture Control", frame)

    # Break with 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
ser.close()
