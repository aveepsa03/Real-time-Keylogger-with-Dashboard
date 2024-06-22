# Real-time-Keylogger-with-Dashboard
------------------------------------
------------------------------------

Project Overview:
This project presents an advanced keylogger application equipped with real-time monitoring capabilities. The keylogger captures both keystrokes and periodic screenshots, providing a comprehensive view of user activity. The captured data is encrypted for security and is visualized on a sophisticated web-based dashboard. This project aims to combine robust user activity tracking with high-level data security and real-time analysis.

Features:

Keylogging

    Keystroke Capture: The keylogger operates stealthily in the background, capturing every keystroke made by the user.
    Data Encryption: All captured keystrokes are encrypted using the Cryptography library to ensure data security and privacy.

Screenshot Capture

    Periodic Screenshots: The application takes screenshots at specified intervals, providing visual context to the keystrokes captured.
    Secure Storage: Screenshots are stored securely in a designated directory, with filenames indicating the timestamp of capture.

Real-time Dashboard

    Interactive Interface: A web-based dashboard built with Flask, HTML, CSS, and JavaScript offers a user-friendly and interactive interface.
    Live Data Feed: The dashboard displays decrypted keystrokes and screenshots in real-time, allowing immediate analysis.
    Organized Display: Keystrokes are displayed in a continuous log, while screenshots are shown in a separate section with timestamps.

Tools and Technologies
Backend

    Python: The core functionality of the keylogger, including keystroke logging and screenshot capturing, is implemented in Python.
    Flask: A lightweight web framework used to develop the server-side of the dashboard.
    Pynput: A Python library used for capturing keystrokes.
    PyAutoGUI: A Python module used for taking screenshots at regular intervals.
    Cryptography: This library ensures that all log data is encrypted and decrypted securely.

Frontend

    HTML/CSS/JavaScript: These technologies are used to create a responsive and interactive dashboard interface.

Prerequisites

    Python 3.x
    Flask
    Pynput
    PyAutoGUI
    Cryptography

Usage

    Starting the Keylogger: Run keylogger.py to start capturing keystrokes and screenshots. Ensure the script is running in the background.
    Viewing Data: Open the dashboard by running app.py and navigating to the specified URL in your browser. The dashboard will display the captured keystrokes and screenshots in real-time.
    Stopping the Keylogger: To stop the keylogger, manually terminate the keylogger.py process.

Security Considerations

    Encryption: All captured data is encrypted using the Fernet symmetric encryption method to ensure that log data remains confidential.
    Data Storage: Keystrokes and screenshots are stored securely on the local machine. Users should ensure that access to these files is restricted.

Future Enhancements

    User Authentication: Implementing authentication for accessing the dashboard to enhance security.
    Advanced Analysis: Adding features for advanced data analysis, such as keyword detection and activity patterns.
    Cloud Integration: Storing logs and screenshots on a cloud server for remote monitoring and analysis.

Conclusion

This project successfully combines keylogging and screenshot capturing with real-time data visualization. It provides a robust tool for monitoring user activity while ensuring data security through encryption. The interactive dashboard enhances usability, making it easier to analyze the captured data in real-time.
