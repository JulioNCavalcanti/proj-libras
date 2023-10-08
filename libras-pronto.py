import cv2
import mediapipe as mp
import math

def put_text(img, text, position=(10, 50), font_scale=1, color=(0, 255, 0), thickness=2):
    cv2.putText(img, text, position, cv2.FONT_HERSHEY_SIMPLEX, font_scale, color, thickness, cv2.LINE_AA)

def calculate_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

video = cv2.VideoCapture(0)
hands = mp.solutions.hands
Hands = hands.Hands(max_num_hands=1)
mpDwaw = mp.solutions.drawing_utils

while True:
    success, img = video.read()

    frameRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = Hands.process(frameRGB)
    handPoints = results.multi_hand_landmarks
    h, w, _ = img.shape
    pontos = []

    if handPoints:
        for points in handPoints:
            mpDwaw.draw_landmarks(img, points, hands.HAND_CONNECTIONS)

            # podemos enumerar esses pontos da seguinte forma
            for id, cord in enumerate(points.landmark):
                cx, cy = int(cord.x * w), int(cord.y * h)
                cv2.putText(img, str(id), (cx, cy + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                pontos.append((cx, cy))

            if len(pontos) >= 21:
                # Calcular e imprimir a distância entre os pontos 8, 12, 16 e 20
                dist_8_12 = calculate_distance(pontos[8], pontos[12])
                dist_12_16 = calculate_distance(pontos[12], pontos[16])
                dist_16_20 = calculate_distance(pontos[16], pontos[20])

                text = f"    Distâncias: 8-12: {dist_8_12:.2f}, 12-16: {dist_12_16:.2f}, 16-20: {dist_16_20:.2f}"
                put_text(img, text)


            # Algoritmo para detectar mão esquerda
            if pontos[1][0] < pontos[0][0]:
                print("Mão: Esquerda")
                # Comparacão letra A
                if (pontos and pontos[8][1] > pontos[5][1]) and (pontos[12][1] > pontos[9][1]) and (pontos[16][1] > pontos[13][1]) and (pontos[20][1] > pontos[17][1]) and (pontos[4][1] < pontos[6][1]) and (pontos[4][0] < pontos[6][0]):
                    text = "Letra: A"
                    put_text(img, text)
                
                # Comparação B
                if (pontos and pontos[8][1] < pontos[7][1]) and (pontos[12][1] < pontos[11][1]) and (pontos[16][1] < pontos[15][1]) and (pontos[20][1] < pontos[18][1]) and (pontos[4][1] > pontos[9][1]) and (pontos[4][0] > pontos[9][0]):
                    if (dist_8_12 < 20 and dist_12_16 < 20 and dist_16_20 < 20):
                        text = "Letra: B"
                        put_text(img, text)

                # Comparacão letra D
                if (pontos and pontos[8][1] < pontos[7][1]) and (pontos[12][1] > pontos[9][1]) and (pontos[16][1] > pontos[13][1]) and (pontos[20][1] > pontos[17][1]) and (pontos[4][0] > pontos [12][0]):
                    text = "Letra: D"
                    put_text(img, text)

                # Comparacão letra I
                if (pontos and pontos[20][1] < pontos[17][1]) and (pontos and pontos[8][1] > pontos[5][1]) and (pontos[12][1] > pontos[9][1]) and (pontos[16][1] > pontos[13][1]) and (pontos[4][0] > pontos[12][0]) and (pontos[4][1] > pontos[14][1]):
                    text = "Letra: I"
                    put_text(img, text)
                
                # Comparacão letra L
                if (pontos and pontos[8][1] < pontos[7][1]) and (pontos[12][1] > pontos[9][1]) and (pontos[16][1] > pontos[13][1]) and (pontos[20][1] > pontos[17][1]) and (pontos[4][1] > pontos[5][1]) and (pontos[4][0] < pontos[3][0]):
                    text = "Letra: L"
                    put_text(img, text)

                # Comparacão letra S
                if (pontos and pontos[8][1] > pontos[5][1]) and (pontos[12][1] > pontos[9][1]) and (pontos[16][1] > pontos[13][1]) and (pontos[20][1] > pontos[17][1]) and (pontos[4][0] > pontos[6][0]) and (pontos[4][1] > pontos[10][1]):
                    text = "Letra: S"
                    put_text(img, text)

                # Comparacão letra Y
                if (pontos and pontos[8][1] < pontos[7][1]) and (pontos[12][1] < pontos[9][1]) and (pontos[16][1] > pontos[13][1]) and (pontos[20][1] > pontos[17][1]) and (pontos[4][0] > pontos [12][0]):
                    text = "Letra: Y"
                    put_text(img, text)

                # Comparacão letra W
                if (pontos and pontos[8][1] < pontos[7][1]) and (pontos[12][1] < pontos[9][1]) and (pontos[16][1] < pontos[13][1]) and (pontos[20][1] > pontos[17][1]) and (pontos[4][0] > pontos [13][0]):
                    text = "Letra: W"
                    put_text(img, text)

            # algoritmo para detectar mão direita
            elif pontos[1][0] > pontos[0][0]:
                print("Mão: Direita")

                # Comparacão letra A
                if (pontos and pontos[8][1] > pontos[5][1]) and (pontos[12][1] > pontos[9][1]) and (pontos[16][1] > pontos[13][1]) and (pontos[20][1] > pontos[17][1]) and (pontos[4][1] < pontos[6][1]) and (pontos[4][0] > pontos[6][0]):
                    text = "Letra: A"
                    put_text(img, text)
                
                # Comparação B
                if (pontos and pontos[8][1] < pontos[7][1]) and (pontos[12][1] < pontos[11][1]) and (pontos[16][1] < pontos[15][1]) and (pontos[20][1] < pontos[18][1]) and (pontos[4][1] > pontos[9][1]) and (pontos[4][0] < pontos[9][0]):
                    text = "Letra: B"
                    put_text(img, text)

                # Comparacão letra D
                if (pontos and pontos[8][1] < pontos[7][1]) and (pontos[12][1] > pontos[9][1]) and (pontos[16][1] > pontos[13][1]) and (pontos[20][1] > pontos[17][1]) and (pontos[4][0] < pontos [12][0]):
                    text = "Letra: D"
                    put_text(img, text)

                # Comparacão letra I
                if (pontos and pontos[20][1] < pontos[17][1]) and (pontos and pontos[8][1] > pontos[5][1]) and (pontos[12][1] > pontos[9][1]) and (pontos[16][1] > pontos[13][1]) and (pontos[4][0] < pontos[12][0]) and (pontos[4][1] > pontos[14][1]):
                    text = "Letra: I"
                    put_text(img, text)
                
                # Comparacão letra L
                if (pontos and pontos[8][1] < pontos[7][1]) and (pontos[12][1] > pontos[9][1]) and (pontos[16][1] > pontos[13][1]) and (pontos[20][1] > pontos[17][1]) and (pontos[4][1] > pontos[5][1]) and (pontos[4][0] > pontos[3][0]):
                    text = "Letra: L"
                    put_text(img, text)

                # Comparacão letra S
                if (pontos and pontos[8][1] > pontos[5][1]) and (pontos[12][1] > pontos[9][1]) and (pontos[16][1] > pontos[13][1]) and (pontos[20][1] > pontos[17][1]) and (pontos[4][0] < pontos[6][0]) and (pontos[4][1] > pontos[10][1]):
                    text = "Letra: S"
                    put_text(img, text)

                # Comparacão letra Y
                if (pontos and pontos[8][1] < pontos[7][1]) and (pontos[12][1] < pontos[9][1]) and (pontos[16][1] > pontos[13][1]) and (pontos[20][1] > pontos[17][1]) and (pontos[4][0] < pontos [12][0]):
                    text = "Letra: Y"
                    put_text(img, text)

                # Comparacão letra W
                if (pontos and pontos[8][1] < pontos[7][1]) and (pontos[12][1] < pontos[9][1]) and (pontos[16][1] < pontos[13][1]) and (pontos[20][1] > pontos[17][1]) and (pontos[4][0] < pontos [13][0]):
                    text = "Letra: W"
                    put_text(img, text)

    cv2.imshow('Imagem', img)
    cv2.waitKey(1)