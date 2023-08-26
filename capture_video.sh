#!/bin/bash

# Redireccionar la salida estándar y de error al archivo "output.log"exec >> output.log 2>&1


echo "Iniciando el script de captura de video ..."

mkdir -p storage

while true; do
    filename="storage/$(date +'%Y%m%d_%H%M%S').mp4"
    echo "  Reiniciando cámara"
    ffmpeg -i /dev/video0 "$filename" &
    ffmpeg_pid=$!
    echo "PID de ffmpeg: $ffmpeg_pid"
    sleep 1800
    echo "Matando el proceso de ffmpeg (PID: $ffmpeg) ..."
    kill "$ffmpeg_pid"
    wait "$ffmpeg_pid"  # Espera a que el proceso se termine adecuadamente.
    echo "Proceso de ffmpeg finalizado."
done
