import tkinter as tk
from tkinter import ttk, messagebox
import serial
import serial.tools.list_ports


class SerialGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Arduino Serial Communication")
        
        # Initialize variables
        self.serial_connection = None
        self.selected_port = tk.StringVar()
        self.selected_baudrate = tk.StringVar(value="9600")
        
        # Create GUI elements
        self.create_widgets()
        self.update_ports()
    
    def create_widgets(self):
        # Textbox for sending data
        self.textbox = tk.Entry(self.root, width=50)
        self.textbox.grid(row=0, column=0, padx=10, pady=10)
        
        # Send button
        self.send_button = tk.Button(self.root, text="Send", command=self.send_data)
        self.send_button.grid(row=0, column=1, padx=10, pady=10)
        
        # Baudrate selection
        tk.Label(self.root, text="Baudrate:").grid(row=1, column=0, sticky=tk.W, padx=10)
        baudrates = ["9600", "14400", "19200", "38400", "57600", "115200"]
        self.baudrate_menu = ttk.Combobox(self.root, textvariable=self.selected_baudrate, values=baudrates, state="readonly")
        self.baudrate_menu.grid(row=1, column=0, padx=10, pady=10)
        
        # COM port selection drop-down
        tk.Label(self.root, text="COM Port:").grid(row=2, column=0, sticky=tk.W, padx=10)
        self.com_port_menu = ttk.Combobox(self.root, textvariable=self.selected_port, state="readonly")
        self.com_port_menu.grid(row=2, column=0, padx=10, pady=10)
        
        # Connect button
        self.connect_button = tk.Button(self.root, text="Connect", command=self.connect_serial)
        self.connect_button.grid(row=2, column=1, padx=10, pady=10)
        
        # Connection status light (Canvas for red/green light)
        self.canvas = tk.Canvas(self.root, width=20, height=20, bg="red")
        self.canvas.grid(row=0, column=2, padx=10, pady=10)
    
    def update_ports(self):
        # Fetch and update available COM ports
        ports = serial.tools.list_ports.comports()
        self.ports_list = [port.device for port in ports]
        
        if self.ports_list:
            self.com_port_menu['values'] = self.ports_list
            self.selected_port.set(self.ports_list[0])
        else:
            messagebox.showerror("Error", "No COM ports found!")
    
    def connect_serial(self):
        # Attempt to establish serial connection
        try:
            self.serial_connection = serial.Serial(self.selected_port.get(), self.selected_baudrate.get())
            self.canvas.config(bg="green")  # Change light to green
            messagebox.showinfo("Success", f"Connected to {self.selected_port.get()} at {self.selected_baudrate.get()} baud.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to connect: {e}")
            self.canvas.config(bg="red")  # Keep light red on failure
    
    def send_data(self):
        # Send data through serial port
        if self.serial_connection and self.serial_connection.is_open:
            data = self.textbox.get()
            self.serial_connection.write(data.encode('utf-8'))
        else:
            messagebox.showerror("Error", "No active serial connection.")
    
    def close_serial(self):
        # Close serial connection on exit
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()

# Main
if __name__ == "__main__":
    root = tk.Tk()
    gui = SerialGUI(root)
    root.protocol("WM_DELETE_WINDOW", gui.close_serial)  # Ensure serial port is closed on exit
    root.mainloop()
