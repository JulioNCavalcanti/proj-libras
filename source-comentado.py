# Importa as bibliotecas necessárias
import cv2
import mediapipe as mp

# Inicializa a captura de vídeo a partir da webcam (0 indica a câmera padrão)
video = cv2.VideoCapture(0)

# Configuração do módulo Hands do Mediapipe para detectar mãos
hands = mp.solutions.hands
Hands = hands.Hands(max_num_hands=1)
mpDwaw = mp.solutions.drawing_utils

# Loop principal para processar continuamente os frames do vídeo
while True:
    # Lê um frame do vídeo
    success, img = video.read()

    # Converte o espaço de cores do frame de BGR para RGB
    frameRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Processa a imagem para encontrar landmarks (pontos característicos) nas mãos
    results = Hands.process(frameRGB)
    handPoints = results.multi_hand_landmarks
    h, w, _ = img.shape
    pontos = []

    # Verifica se landmarks foram encontrados
    if handPoints:
        # Desenha os landmarks e conexões na imagem
        for points in handPoints:
            mpDwaw.draw_landmarks(img, points, hands.HAND_CONNECTIONS)

            # Coleta as coordenadas (x, y) dos landmarks e exibe o ID de cada landmark
            for id, cord in enumerate(points.landmark):
                cx, cy = int(cord.x * w), int(cord.y * h)
                cv2.putText(img, str(id), (cx, cy + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                pontos.append((cx, cy))

        # Comparação para detectar gestos de letras do alfabeto
        # Cada bloco de comparação verifica se os landmarks estão em posições específicas para cada letra
        if (pontos and pontos[8][1] > pontos[5][1]) and (pontos[12][1] > pontos[9][1]) and (pontos[16][1] > pontos[13][1]) and (pontos[20][1] > pontos[17][1]) and (pontos[4][1] < pontos[6][1]) and (pontos[4][0] < pontos[6][0]):
            print("Letra A")
        elif (pontos and pontos[8][1] < pontos[7][1]) and (pontos[12][1] < pontos[11][1]) and (pontos[16][1] < pontos[15][1]) and (pontos[20][1] < pontos[18][1]) and (pontos[4][1] > pontos[9][1]) and (pontos[4][0] > pontos[9][0]):
            print("Letra B")
        # ... (repete para outras letras)

    # Exibe a imagem com as marcações
    cv2.imshow('Imagem', img)
    
    # Aguarda uma tecla (1 milissegundo) e verifica se a tecla 'q' foi pressionada para encerrar o loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera os recursos
video.release()
cv2.destroyAllWindows()
