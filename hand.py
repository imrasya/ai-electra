import cv2
import mediapipe as mp
import screen_brightness_control as sbc

# Inisialisasi MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

# Fungsi untuk menghitung jarak antara dua titik
def calculate_distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

# Membuka webcam
cap = cv2.VideoCapture(0)

# Variabel untuk menyimpan jarak sebelumnya untuk kedua tangan
prev_distance_right = None
prev_distance_left = None

while cap.isOpened():
    success, img = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    # Membalik gambar horizontal agar tidak mirror
    img = cv2.flip(img, 1)

    # Mengubah gambar ke RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    # Memeriksa apakah ada tangan yang terdeteksi
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Dapatkan label tangan (kanan/kiri)
            hand_label = results.multi_handedness[0].classification[0].label

            # Dapatkan landmark jari-jari tangan
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

            # Konversi ke koordinat piksel
            h, w, c = img.shape
            thumb_tip_coords = (int(thumb_tip.x * w), int(thumb_tip.y * h))
            index_tip_coords = (int(index_tip.x * w), int(index_tip.y * h))

            # Hitung jarak antara jempol dan telunjuk
            distance = calculate_distance(thumb_tip_coords, index_tip_coords)

            # Memeriksa dan memproses tangan kanan
            if hand_label == 'Right':
                if prev_distance_right is not None:
                    current_brightness = sbc.get_brightness(display=0)[0]

                    # Jika jarak saat ini lebih besar dari jarak sebelumnya, tambahkan kecerahan
                    if distance > prev_distance_right:
                        new_brightness = min(current_brightness + 5, 100)  # tambahkan kecerahan dengan nilai 5%
                        sbc.set_brightness(new_brightness, display=0)
                    # Jika jarak saat ini lebih kecil dari jarak sebelumnya, kurangi kecerahan
                    elif distance < prev_distance_right:
                        new_brightness = max(current_brightness - 5, 0)  # kurangi kecerahan dengan nilai 5%
                        sbc.set_brightness(new_brightness, display=0)

                prev_distance_right = distance

            # Memeriksa dan memproses tangan kiri
            elif hand_label == 'Left':
                if prev_distance_left is not None:
                    current_brightness = sbc.get_brightness(display=0)[0]

                    # Jika jarak saat ini lebih besar dari jarak sebelumnya, tambahkan kecerahan
                    if distance > prev_distance_left:
                        new_brightness = min(current_brightness + 5, 100)  # tambahkan kecerahan dengan nilai 5%
                        sbc.set_brightness(new_brightness, display=0)
                    # Jika jarak saat ini lebih kecil dari jarak sebelumnya, kurangi kecerahan
                    elif distance < prev_distance_left:
                        new_brightness = max(current_brightness - 5, 0)  # kurangi kecerahan dengan nilai 5%
                        sbc.set_brightness(new_brightness, display=0)

                prev_distance_left = distance

            # Gambar landmark tangan dan sambungan
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Menampilkan gambar
    cv2.imshow("Hand Detection", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
