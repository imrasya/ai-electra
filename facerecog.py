import face_recognition
import cv2
import threading
import os

def facerecog(q):
    video_capture = cv2.VideoCapture(0)  # Gunakan 0 untuk kamera default, atau berikan path file video

    known_face_encodings = []
    known_face_names = []

    # Baca nama dari file name.txt
    with open("name.txt", "r") as file:
        names = file.readlines()
        for name in names:
            known_face_names.append(name.strip())

    # Cache face encodings
    for name in known_face_names:
        face_path = f"faces/{name}.jpg"
        if os.path.exists(face_path):
            face_image = face_recognition.load_image_file(face_path)
            face_encoding = face_recognition.face_encodings(face_image)[0]
            known_face_encodings.append(face_encoding)
        else:
            # Jika file tidak ada, ambil frame dari kamera, simpan dan tambahkan encoding
            while True:
                ret, frame = video_capture.read()
                if not ret:
                    continue
                # Deteksi wajah pada frame
                face_locations = face_recognition.face_locations(frame)
                if face_locations:
                    # Simpan frame sebagai file gambar
                    cv2.imwrite(face_path, frame)
                    # Tambahkan encoding ke daftar yang diketahui
                    face_encoding = face_recognition.face_encodings(frame, face_locations)[0]
                    known_face_encodings.append(face_encoding)
                    break
            # Tambahkan nama ke name.txt
            with open("name.txt", "a") as file:
                file.write(f"{name}\n")

    def process_frames():
        frame_count = 0
        while True:
            ret, frame = video_capture.read()
            if not ret:
                break

            # Perkecil ukuran frame jika besar
            if frame.shape[1] > 800:  # Misalnya, hanya perkecil jika lebar frame melebihi 800 piksel
                frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

            frame_count += 1

            if frame_count % 5 == 0:  # Process every 5 frames
                face_locations = face_recognition.face_locations(frame)
                face_encodings = face_recognition.face_encodings(frame, face_locations)

                for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                    name = "Unknown"

                    if True in matches:
                        match_index = matches.index(True)
                        name = known_face_names[match_index]

                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                    cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)

                cv2.imshow('Video', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    thread = threading.Thread(target=process_frames)
    thread.start()

    thread.join()

    video_capture.release()
    cv2.destroyAllWindows()

# Pastikan folder "faces" ada
if not os.path.exists("faces"):
    os.makedirs("faces")

facerecog("iwak")
