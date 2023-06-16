import cv2

# Abre o arquivo de video
input_video = cv2.VideoCapture(0)

# Checa se foi possivel abrir o arquivo
if not input_video.isOpened():
    print("Error opening video file")
    exit(1)

# Variáveis que guardam o tamanho do video
width = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Cria o arquivo de video de output
output_video = cv2.VideoWriter(
    "./out.avi", cv2.VideoWriter_fourcc(*"DIVX"), 24, (width, height)
)

print("Vídeo sendo iniciado, pressione 'q' para encerrar")

# Loop de leitura frame por frame
while True:
    # Lê o frame
    ret, frame = input_video.read()

    # Erro caso nao consiga ler o frame
    if not ret:
        break

    # Transforma o frame em escala de cinza
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Cria uma variável com o modelo de detecção de faces do OpenCV
    face_classifier = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    # Detecta faces
    face = face_classifier.detectMultiScale(
        gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
    )

    # Desenha um retângulo preto em volta da face
    for x, y, w, h in face:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), 4)

    # Exibe o frame
    cv2.imshow("Video Playback", frame)

    # Escreve o frame no vídeo output
    output_video.write(frame)

    # Encerra o loop caso a tecla "q" seja pressionada
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

# Fecha tudo
output_video.release()
input_video.release()
cv2.destroyAllWindows()