from flask import Flask, request, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Allow all origins

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Ensure the folder exists


@app.route('/upload', methods=['POST'])
def upload_video():
    video = request.files.get('video')
    if not video:
        return 'No video uploaded', 400

    filename = video.filename
    video.save(os.path.join(UPLOAD_FOLDER, filename))

    # wahaj code
    # import time
    # time.sleep(600)

    return 'Video uploaded successfully', 200


@app.route('/uploads/<filename>', methods=['GET'])
def get_video(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


if __name__ == '__main__':
    app.run(port=5000)
