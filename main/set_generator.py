import cv2
import os
import sys

# Получение ID из аргументов командной строки
if len(sys.argv) < 2:
    print("Usage: python set_generator.py <id>")
    sys.exit(1)

face_id = sys.argv[1]  # ID пользователя

current_dir = os.path.dirname(__file__)
face_cascade = cv2.CascadeClassifier(
    os.path.abspath(os.path.join(current_dir, "..", "CascadeHaar", "haarcascade_frontalface_alt2.xml"))
)
cap = cv2.VideoCapture(0)
count = 0

while True:
    img = cap.read()[1]
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        # Сохраняем изображения в папке dataset
        cv2.imwrite(f"dataset/{face_id}.{count}.jpg", roi_gray)
        count += 1
        print(f"Set {count} images")

    cv2.imshow("img", img)
    k = cv2.waitKey(10)

    if k == 27:  # Нажатие клавиши Esc для выхода
        break
    elif count >= 100:  # Завершаем, если собрано 100 изображений
        print("Done!")
        break