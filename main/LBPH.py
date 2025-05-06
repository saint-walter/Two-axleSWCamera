import cv2, serial, os

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
names = ["Reptile", "Me", "Artem", "None", "None"]
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, img = cam.read()
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(int(minW), int(minH)))
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)
        center_x = int(x+w/2)
        center_y = int(y+h/2)
        cv2.circle(img, (center_x, center_y), 3, (0,255,255), 3)
        line_result = "P\n"+str(center_x)+"\nT\n"+str(center_y)
        uno.write(line_result.encode())
        print(uno.readline().decode("UTF-8"))
        id, confidence = recognizer.predict(gray[y:y+h, x:x+w])
        print(confidence)
        if(confidence < 40):
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
            cv2.putText(img, str(confidence), (x+5, y+h-5), font, 1, (255,255,0),1)
        else:
            id = names[0]
        cv2.putText(img, str(id), (x+5, y-5), font, 1, (255,255, 255),2)
    cv2.imshow("camera", img)
    cv2.waitKey(10)
