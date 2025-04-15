import cv2, os
current_dir = os.path.dirname(__file__)
face_cascede = cv2.CascadeClassifier(os.path.abspath(os.path.join(current_dir, "..", "CascadeHaar", "haarcascade_frontalface_alt2.xml")))
cap = cv2.VideoCapture(0)
face_id = input("\n Input ID ====>")
count = 0
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascede.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,255,0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        cv2.imwrite("dataset/."+ str(face_id) + '.' + str(count)+ ".jpg", gray[y:y + h, x:x + w])
        count += 1
        print("set "+str(count)+" images")
    cv2.imshow("img", img)
    k = cv2.waitKey(10)
    if k == 27:
        break
    elif count >= 100:
        print("Done!")
        break