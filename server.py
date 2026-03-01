from flask import Flask, request
from datetime import datetime
import os

app = Flask(__name__)

UPLOAD_FOLDER = '/home/sree/Desktop/fileupload/uploads'
SCRIPT_FILE = os.path.join(UPLOAD_FOLDER, 'script.txt')

# Ensure uploads folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/uploads', methods=['POST'])
def append_text():
    text = request.form.get('text')

    if not text:
        return "No text provided.", 400

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(SCRIPT_FILE, 'a') as f:
        f.write(f"[{timestamp}] {text}\n")

    return "Text appended successfully.", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
