import cv2
import serial
import os
import sys

# Получение ID и Name из аргументов командной строки
if len(sys.argv) < 3:
    print("Usage: python LBPH.py <id> <name>")
    sys.exit(1)

user_id = int(sys.argv[1])
user_name = sys.argv[2]

current_dir = os.path.dirname(__file__)
comPort = "COM9"
baudrate = 9600
uno = serial.Serial(comPort, baudrate, timeout=0.1)
face = cv2.CascadeClassifier(os.path.abspath(os.path.join(current_dir, "..", "CascadeHaar", "haarcascade_frontalface_alt2.xml")))
recognizer = cv2.face.LBPHFaceRecognizer.create()
minW = 30
minH = 30
recognizer.read('model/trainer.yml')
faceCascade = cv2.CascadeClassifier(os.path.abspath(os.path.join(current_dir, "..", "CascadeHaar", "haarcascade_frontalface_alt2.xml")))
font = cv2.FONT_HERSHEY_SIMPLEX

# Статический массив имен
names = ["Unknown"] * 100  # Максимум 100 записей, можно увеличить размер по необходимости
names[user_id] = user_name  # Записываем имя в ячейку с индексом ID

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, img = cam.read()
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(int(minW), int(minH)))
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        center_x = int(x + w / 2)
        center_y = int(y + h / 2)
        cv2.circle(img, (center_x, center_y), 3, (0, 255, 255), 3)
        line_result = "P\n" + str(center_x) + "\nT\n" + str(center_y)
        uno.write(line_result.encode())
        print(uno.readline().decode("UTF-8"))
        id, confidence = recognizer.predict(gray[y:y + h, x:x + w])
        print(confidence)
        if confidence < 40:
            id_name = names[id]  # Получаем имя из статического массива
            confidence = "  {0}%".format(round(100 - confidence))
            cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)
        else:
            id_name = "Unknown"
        cv2.putText(img, str(id_name), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
    cv2.imshow("camera", img)
    cv2.waitKey(10)