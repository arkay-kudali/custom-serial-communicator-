custom-serial-communicator

Simple Python GUI tool for serial communication with microcontrollers such as Arduino, ESP32, and other UART-based boards.

The program is built using PyQt5 and pyserial and allows sending commands and reading serial output from connected devices.

Latest version: v1.8

Features

GUI based serial communication

Automatic COM port detection

Baudrate selection

Send serial commands

Receive serial data

Connect / Disconnect control

Port refresh button

Clear output window

Repository Structure
custom-serial-communicator/

application/
    executable versions (.exe)

SERIAL_COM_1_1.py
SERIAL_COM_1_2.py
SERIAL_COM_1_3.py
SERIAL_COM_1_4.pyw
SERIAL_COM_1_5.pyw
SERIAL_COM_1_6.pyw
SERIAL_COM_1_7.pyw
SERIAL_COM_1_8.py   ← latest version

README.md

Older versions are kept in the repository for reference.

Requirements

Python 3.8+

Required libraries:

PyQt5

pyserial

Install Dependencies
Windows

Open Command Prompt:

pip install PyQt5 pyserial
Linux (Ubuntu / Debian)
sudo apt update
sudo apt install python3-pip
pip3 install PyQt5 pyserial
macOS
pip3 install PyQt5 pyserial
Running the Program

Run the latest version:

python SERIAL_COM_1_8.py

or

python3 SERIAL_COM_1_8.py
Using the Application

Connect your microcontroller via USB.

Select the COM port from the dropdown.

Choose the baudrate matching your device.

Click Connect.

Enter text in the input box.

Click Send to transmit data.

Incoming data will appear in the output window.

Hardware Tested

Works with boards such as:

Arduino Uno

Arduino Nano

ESP32

ESP8266

Other UART devices

Python Libraries Used
PyQt5
pyserial
serial.tools.list_ports
Notes

The application auto-refreshes available serial ports.

The GUI indicates connection status using a red / green indicator.

Multiple versions are included in this repository to track development progress.
