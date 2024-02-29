import tkinter as tk
import subprocess

# Global variable to store the model subprocess
model_process = None

# Function to start the model
def start_model():
    global model_process
    try:
        if model_process is None:
            # Start the model script as a separate process
            model_process = subprocess.Popen(["python", "drowsiness detection.py"])
            start_button.config(state=tk.DISABLED)
            stop_button.config(state=tk.NORMAL)
    except Exception as e:
        print(f"Error starting the model: {str(e)}")

# Function to close the model
def close_model():
    global model_process
    try:
        if model_process is not None:
            # Terminate the model process
            model_process.terminate()
            model_process.wait()
            model_process = None
            start_button.config(state=tk.NORMAL)
            stop_button.config(state=tk.DISABLED)
    except Exception as e:
        print(f"Error closing the model: {str(e)}")

# Create a tkinter window
window = tk.Tk()
window.title("Model Controller")

# Create a button to start the model
start_button = tk.Button(window, text="Start Model", command=start_model)
start_button.pack(padx=20, pady=10)

# Create a button to close the model
stop_button = tk.Button(window, text="Close Model", command=close_model, state=tk.DISABLED)
stop_button.pack()

# Start the GUI main loop
window.mainloop()
