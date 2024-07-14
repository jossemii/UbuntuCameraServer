import os
import subprocess
from multiprocessing import Process
from flask import Flask, render_template, send_from_directory

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

def run_flask():
    app.run(host='0.0.0.0', port=5000)

def capture_video():
    os.makedirs('storage', exist_ok=True)
    while True:
        filename = f"storage/{time.strftime('%Y%m%d_%H%M%S')}.mp4"
        print(f"Reiniciando cámara, guardando en {filename}")
        process = subprocess.Popen(['ffmpeg', '-i', '/dev/video0', filename])
        time.sleep(1800)
        print(f"Matando el proceso de ffmpeg (PID: {process.pid}) ...")
        process.terminate()
        process.wait()
        print("Proceso de ffmpeg finalizado.")

if __name__ == '__main__':
    import time
    from multiprocessing import Process

    flask_process = Process(target=run_flask)
    capture_process = Process(target=capture_video)

    flask_process.start()
    capture_process.start()

    flask_process.join()
    capture_process.join()
