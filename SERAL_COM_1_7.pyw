import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, 
    QPushButton, QLabel, QComboBox, QGridLayout, QFrame, QTextEdit
)
from PyQt5.QtCore import Qt, QTimer, QThread, pyqtSignal
import serial
import serial.tools.list_ports


class SerialReader(QThread):
    data_received = pyqtSignal(str)

    def __init__(self, serial_connection):
        super().__init__()
        self.serial_connection = serial_connection
        self.running = True

    def run(self):
        while self.running:
            if self.serial_connection and self.serial_connection.is_open:
                try:
                    data = self.serial_connection.readline().decode('utf-8').strip()
                    if data:
                        self.data_received.emit(data)
                except Exception:
                    pass

    def stop(self):
        self.running = False
        self.wait()


class SerialGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Arduino Serial Communication")
        
        # Initialize variables
        self.serial_connection = None
        self.selected_port = ""
        self.selected_baudrate = "9600"
        self.is_connected = False
        self.ports_list = []  # Initialize the ports_list attribute
        self.serial_reader = None
        
        # Set up main layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        
        # Create GUI elements
        self.create_widgets()
        self.update_ports()

        # Setup timer for auto-refreshing COM ports
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_ports)
        self.timer.start(1000)  # Refresh every second

    def create_widgets(self):
        grid_layout = QGridLayout()
        
        # Textbox for sending data
        self.textbox = QLineEdit(self)
        grid_layout.addWidget(self.textbox, 0, 0, 1, 2)
        
        # Send button
        self.send_button = QPushButton("Send", self)
        self.send_button.clicked.connect(self.send_data)
        grid_layout.addWidget(self.send_button, 0, 2)
        
        # Baudrate selection
        self.baudrate_label = QLabel("Baudrate:", self)
        grid_layout.addWidget(self.baudrate_label, 1, 0)
        
        baudrates = ["9600", "14400", "19200", "38400", "57600", "115200"]
        self.baudrate_menu = QComboBox(self)
        self.baudrate_menu.addItems(baudrates)
        self.baudrate_menu.setCurrentText(self.selected_baudrate)
        self.baudrate_menu.currentIndexChanged.connect(self.update_baudrate)
        grid_layout.addWidget(self.baudrate_menu, 1, 1)
        
        # COM port selection drop-down
        self.port_label = QLabel("COM Port:", self)
        grid_layout.addWidget(self.port_label, 2, 0)
        
        self.com_port_menu = QComboBox(self)
        self.com_port_menu.currentIndexChanged.connect(self.update_port)
        grid_layout.addWidget(self.com_port_menu, 2, 1)
        
        # Connect button
        self.connect_button = QPushButton("Connect", self)
        self.connect_button.clicked.connect(self.toggle_connection)
        grid_layout.addWidget(self.connect_button, 3, 1)
        
        # Connection status light (Frame for red/green light)
        self.status_light = QFrame(self)
        self.status_light.setFixedSize(20, 20)
        self.status_light.setStyleSheet("background-color: red; border-radius: 10px;")
        grid_layout.addWidget(self.status_light, 0, 3)

        # Refresh button
        self.refresh_button = QPushButton("Refresh Ports", self)
        self.refresh_button.clicked.connect(self.update_ports)
        grid_layout.addWidget(self.refresh_button, 2, 2)

        # Clear button to clear the display area
        self.clear_button = QPushButton("Clear Monitor", self)
        self.clear_button.clicked.connect(self.clear_monitor)
        grid_layout.addWidget(self.clear_button, 3, 2)
        
        # Display area for received data
        self.text_display = QTextEdit(self)
        self.text_display.setReadOnly(True)  # Make it read-only
        self.layout.addLayout(grid_layout)
        self.layout.addWidget(self.text_display)
    
    def update_ports(self):
        # Fetch and update available COM ports
        ports = serial.tools.list_ports.comports()
        ports_list = [port.device for port in ports]
        
        if ports_list != self.ports_list:
            self.ports_list = ports_list
            self.com_port_menu.clear()
            if self.ports_list:
                self.com_port_menu.addItems(self.ports_list)
                self.selected_port = self.ports_list[0]
            else:
                self.selected_port = ""
                self.status_light.setStyleSheet("background-color: red;")
    
    def update_baudrate(self):
        self.selected_baudrate = self.baudrate_menu.currentText()
    
    def update_port(self):
        self.selected_port = self.com_port_menu.currentText()
    
    def toggle_connection(self):
        if self.is_connected:
            self.disconnect_serial()
        else:
            self.connect_serial()
    
    def connect_serial(self):
        # Attempt to establish serial connection
        try:
            self.serial_connection = serial.Serial(self.selected_port, self.selected_baudrate)
            self.status_light.setStyleSheet("background-color: green; border-radius: 10px;")
            self.connect_button.setText("Disconnect")
            self.is_connected = True
            
            # Start the thread to read incoming data
            self.serial_reader = SerialReader(self.serial_connection)
            self.serial_reader.data_received.connect(self.display_data)
            self.serial_reader.start()

        except Exception:
            self.status_light.setStyleSheet("background-color: red; border-radius: 10px;")
    
    def disconnect_serial(self):
        # Close the serial connection and stop the reader thread
        if self.serial_reader:
            self.serial_reader.stop()
            self.serial_reader = None
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()
        self.status_light.setStyleSheet("background-color: red; border-radius: 10px;")
        self.connect_button.setText("Connect")
        self.is_connected = False
    
    def send_data(self):
        # Send data through serial port
        if self.serial_connection and self.serial_connection.is_open:
            data = self.textbox.text()
            self.serial_connection.write(data.encode('utf-8'))
    
    def display_data(self, data):
        # Display received data in the text display
        self.text_display.append(data)

    def clear_monitor(self):
        # Clear the display area
        self.text_display.clear()

    def closeEvent(self, event):
        # Ensure serial port is closed on exit
        self.disconnect_serial()
        event.accept()

# Main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = SerialGUI()
    gui.show()
    sys.exit(app.exec_())
