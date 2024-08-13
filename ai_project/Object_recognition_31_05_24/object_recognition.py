import cv2

face_cascade = cv2.CascadeClassifier('faces.xml')
eye_cascade = cv2.CascadeClassifier('eye.xml')
webcam = cv2.VideoCapture(0)
# webcam.set(3, 300)
webcam.set(4, 500)

while True:
    success, img = webcam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    """распознаем лицо"""
    for (fx, fy, fw, fh) in faces:
        # cv2.rectangle(img, (fx, fy), (fx + fw, fy + fh), (0, 0, 250), thickness=1) # рамка определения лица
        roi_gray = gray[fy:fy + fh, fx:fx + fw]
        roi_color = img[fy:fy + fh, fx:fx + fw]
        eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=3.3, minNeighbors=5)

        """поиск на лице распознаем глаза"""
        for (ex, ey, ew, eh) in eyes:
            # cv2.rectangle(roi_color, (0, ey), (roi_color.shape[0], ey + eh), (0, 255, 0), 1) # рамка определения глаз
            roi_color2 = roi_color[ey:ey + eh, 0:roi_color.shape[0]]
            roi_color2 = cv2.GaussianBlur(roi_color2, (31, 31), 21)
            roi_color[ey:ey + eh, 0:roi_color.shape[0]] = roi_color2

    cv2.imshow('screen.jpg', img) # отображаем видео на экране
    if cv2.waitKey(1) & 0xFF == ord('q'): # закрывваем просмотр по клавище "q"
        break
"""сохраням картинку в файл при закрыти окна"""
webcam.release()
cv2.imwrite('screen1qqqq.jpg', img)