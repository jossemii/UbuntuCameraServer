import cv2

def main(index=0):
    print(f"Abre la cámara. {index} indica el primer dispositivo de video, que generalmente es la cámara en una Raspberry Pi.")
    cap = cv2.VideoCapture(index)

    if not cap.isOpened():
        print("Error al abrir la cámara.")
        return

    while True:
        # Lee un fotograma de la cámara.
        ret, frame = cap.read()

        if not ret:
            print("Error al capturar el fotograma.")
            break

        # Muestra el fotograma en una ventana.
        cv2.imshow('Camera', frame)

        # Presiona 'q' para salir del bucle y cerrar la ventana.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Libera la cámara y cierra la ventana al finalizar.
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    for i in range(20):
        main(i)
