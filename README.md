# AI-Powered IoT Projects with Hand Gesture Control

## Overview

This repository contains AI-integrated IoT projects where hand gestures are used to control various IoT applications, such as LED lights and other smart devices. By leveraging computer vision, deep learning, and microcontroller-based hardware, these projects demonstrate innovative ways to interact with IoT systems.

## Features

- **Hand Gesture Recognition**: Detects hand gestures using OpenCV and MediaPipe.
- **IoT Integration**: Uses Raspberry Pi Pico WH to control IoT devices.
- **Wi-Fi Communication**: Establishes seamless connectivity between AI-based gesture recognition and IoT hardware.
- **Voice Feedback**: Provides real-time feedback on detected gestures.
- **Expandable Framework**: Can be extended to control multiple IoT applications like fans, motors, and smart appliances.

## Implemented Projects

### 1. **Hand Gesture Controlled LED**

- **Five Fingers** → Turns the LED **ON**
- **Zero Fingers** → Turns the LED **OFF**
- Uses **Raspberry Pi Pico WH** and **Python (OpenCV + MediaPipe)** for real-time gesture recognition.

### 2. **Gesture-Based IoT Controller**

- Controls IoT devices such as fans, lights, and smart appliances using hand gestures.
- Uses a **Wi-Fi connection** to communicate with the Raspberry Pi Pico WH.
- Supports **real-time monitoring** through serial communication and cloud integration.

### 3. **Gesture-Controlled System Brightness**

- Adjusts system brightness based on finger movement.
- Detects thumb and index finger distance to increase or decrease brightness gradually.

### 4. **AI-Based Gesture-Controlled Shorts/Reels Scroller**

- **Index Finger Up** → Scrolls **down** (Next Short/Reel)
- **Hand Down Gesture** → Scrolls **up** (Previous Short/Reel)
- **Show Five Fingers** → Pauses the Reel
- Uses PyAutoGUI for system control.

### 5. **Face Detection with Gesture Control**

- Displays a message **"Hi U Look Nice"** when a face is detected in the camera feed.
- Shows the recognized gesture at the bottom of the output screen.

## Technologies Used

- **Programming Language**: Python
- **Computer Vision**: OpenCV, MediaPipe
- **Machine Learning**: TensorFlow Lite (for efficient gesture recognition)
- **Hardware**: Raspberry Pi Pico WH, LEDs, IoT Sensors
- **Communication Protocols**: Serial, Wi-Fi (MicroPython on Pico WH)

## Installation & Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/ai-iot-gesture-control.git
   cd ai-iot-gesture-control
   ```
2. Install dependencies:
   ```sh
   pip install opencv-python mediapipe pyserial socket
   ```
3. Upload the MicroPython script to Raspberry Pi Pico WH using **Thonny IDE**.
4. Run the AI gesture recognition script on your PC:
   ```sh
   python gesture_ai.py
   ```
5. Ensure Raspberry Pi Pico WH is connected to the same Wi-Fi network.

## Future Enhancements

- Adding more complex gestures for **multi-device control**.
- Implementing **voice commands** alongside gesture recognition.
- Enhancing **accuracy** with deep learning models.
- Integrating **Cloud-based IoT platforms** for remote control.

## Contributing

Contributions are welcome! Feel free to submit pull requests or report issues.

## License

This project is licensed under the **open source**.

---

**Author**: Ashik SM\
**Contact**: ashiksm01\@gamil.com

