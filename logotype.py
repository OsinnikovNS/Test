import cv2
import numpy as np

photo = np.zeros(shape=(600, 600, 3), dtype='uint8')
# фон градиент
for i in range(150):
    cv2.rectangle(photo, (i, i), (photo.shape[0]-i, photo.shape[0]-i), (250, 201-i, 250-i), thickness=cv2.FILLED)

# формирование логотипа
cv2.circle(photo, (photo.shape[1]//2, photo.shape[0]//2), 100, (255, 255, 255), 3)
cv2.ellipse(img=photo, center=(photo.shape[1]//2, photo.shape[0]//2), axes=(40, 40), angle=0., startAngle=0, endAngle=180, color=(0,255,0),thickness=3)
cv2.ellipse(img=photo, center=(photo.shape[1]//2, photo.shape[0]//2), axes=(20, 20), angle=0., startAngle=0, endAngle=180, color=(0,255,0),thickness=3)
cv2.line(photo, (260, 260), (260, 300), (255, 0, 0), thickness=3)
cv2.line(photo, (280, 260), (280, 300), (255, 0, 0), thickness=3)
cv2.line(photo, (320, 260), (320, 300), (255, 0, 0), thickness=3)
cv2.line(photo, (340, 260), (340, 300), (255, 0, 0), thickness=3)
cv2.line(photo, (260, 260), (280, 260), (0, 0, 255), thickness=3)
cv2.line(photo, (320, 260), (340, 260), (0, 0, 255), thickness=3)

cv2.imshow('Urban Logo', photo)
cv2.waitKey(0)
