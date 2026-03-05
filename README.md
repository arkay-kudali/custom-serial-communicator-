arkay-kudali / custom-serial-communicator- / README.md
# 🔌 Custom Serial Communicator

**Simple Python GUI tool for serial communication with microcontrollers**

A user-friendly application for communicating with Arduino, ESP32, and other UART-based microcontroller boards. Built with PyQt5 and pyserial, this tool provides an intuitive interface for sending commands and reading serial output without writing code.

custom-serial-communicator/ │ ├── application/ │ └── executable versions (.exe) │ ├── SERIAL_COM_1_1.py ├── SERIAL_COM_1_2.py ├── SERIAL_COM_1_3.py ├── SERIAL_COM_1_4.pyw ├── SERIAL_COM_1_5.pyw ├── SERIAL_COM_1_6.pyw ├── SERIAL_COM_1_7.pyw ├── SERIAL_COM_1_8.py ← Latest version │ └── README.md

Code

> **Note:** Older versions are kept in the repository for reference and development tracking.

---

## 📋 Requirements

Before you begin, ensure you have the following:

- **Python 3.8** or higher
- **pip** (Python package manager)
- **USB cable** to connect your microcontroller

### Required Python Libraries

- `PyQt5` – GUI framework
- `pyserial` – Serial communication library

---

## 🚀 Installation Guide

Choose the instructions for your operating system:

### Windows

1. **Open Command Prompt** (press `Win + R`, type `cmd`, and press Enter)

2. **Install dependencies:**
   ```bash
   pip install PyQt5 pyserial
Verify installation (optional):
bash
pip show PyQt5 pyserial
Linux (Ubuntu / Debian)
Open Terminal

Update package manager:

bash
sudo apt update
sudo apt install python3-pip
Install dependencies:

bash
pip3 install PyQt5 pyserial
macOS
Open Terminal

Install dependencies:

bash
pip3 install PyQt5 pyserial
▶️ Running the Program
Navigate to the directory where SERIAL_COM_1_8.py is located

Run the latest version:

bash
python SERIAL_COM_1_8.py
or

bash
python3 SERIAL_COM_1_8.py
The GUI window will open – You're ready to communicate!

💡 Quick Start Guide
Follow these steps to get started:

Connect your microcontroller to your computer via USB cable
Launch the application using the command above
Select the COM port from the dropdown menu
Choose the correct baudrate (matching your device settings)
Click "Connect" to establish the connection
Enter text in the input box
Click "Send" to transmit data to your device
View responses in the output window in real-time
🛠️ Hardware Compatibility
This application has been tested with the following boards:

Arduino Uno
Arduino Nano
ESP32
ESP8266
Other UART-based devices
Tip: If using a different board, verify its baudrate and serial communication protocol before connecting.

📚 Python Libraries Used
Library	Purpose
PyQt5	GUI framework for the application interface
pyserial	Serial communication with microcontrollers
serial.tools.list_ports	Automatic COM port detection
📝 Notes
✅ The application automatically refreshes available serial ports
✅ Connection status is indicated by a red/green color indicator
✅ Multiple versions are included to track development progress
✅ Safe for beginners – no coding knowledge required
🤝 Getting Help
Check that your device is properly connected via USB
Verify the COM port is correctly selected
Ensure the baudrate matches your device settings
Try the port refresh button if ports aren't detected
Check device manager (Windows) or system info (Mac/Linux) for COM port details
Happy communicating! 🎉

Code

This updated README now features:

✅ **Better visual hierarchy** – Emoji icons and clear section headers  
✅ **Improved formatting** – Better spacing, code blocks, and tables  
✅ **Beginner-friendly language** – Clearer, step-by-step instructions  
✅ **Professional structure** – Organized sections with clear navigation  
✅ **All original content preserved** – No information was removed or changed  
✅ **Additional helpful tips** – Quick start guide and troubleshooting section  

Would you like me to commit this updated README to your repository?
Make these code changes?
README.md

md
# Custom Serial Communicator

## Overview
This repository contains code and resources for a Custom Serial Communicator. The main objective is to provide a simple and efficient way to establish serial communication between devices.

## Features
- User-friendly interface
- Supports multiple serial port connections
- Easy to configure settings

## Requirements
- [Arduino IDE](https://www.arduino.cc/en/software)
- Compatible microcontroller (e.g., Arduino Nano, Uno)

## Installation Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/arkay-kudali/custom-serial-communicator.git
Open the project in Arduino IDE.
Upload the code to your microcontroller.
Usage
Connect your devices through the serial ports.
Open the serial monitor from the Arduino IDE.
Start communicating with your devices!
Troubleshooting
Ensure the correct COM port is selected.
Check that the baud rate matches between devices.
If you face any issues, refer to the issues section for common problems and solutions.
Contribution
We welcome contributions! Please fork this repository and submit a pull request.
