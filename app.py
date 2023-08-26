from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Ruta al directorio de videos
videos_directory = os.path.join(os.getcwd(), 'storage')

@app.route('/')
def index():
    video_files = [file for file in os.listdir(videos_directory) if file.endswith('.mp4')]
    return render_template('index.html', video_files=video_files)


@app.route('/videos/<filename>')
def stream_video(filename):
    return send_from_directory(videos_directory, filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
