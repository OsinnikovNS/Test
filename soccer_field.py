import cv2
import numpy as np

photo = np.zeros(shape=(600, 1200, 3), dtype='uint8')
# color field with bonus gradient
for i in range(100):
    cv2.rectangle(photo, (i, i), (photo.shape[1]-i, photo.shape[0]-i), (22, 201, 22+i), thickness=cv2.FILLED)

# emblem soccer club
cv2.circle(photo, (photo.shape[1]//2, photo.shape[0]//2), 80, (255, 255, 255), 2)
cv2.ellipse(img=photo, center=(photo.shape[1]//2, photo.shape[0]//2), axes=(40, 40), angle=0., startAngle=0, endAngle=180, color=(0,255,0),thickness=3)
cv2.ellipse(img=photo, center=(photo.shape[1]//2, photo.shape[0]//2), axes=(20, 20), angle=0., startAngle=0, endAngle=180, color=(0,255,0),thickness=3)
cv2.line(photo, (560, 270), (560, 300), (255, 0, 0), thickness=3)
cv2.line(photo, (580, 270), (580, 300), (255, 0, 0), thickness=3)
cv2.line(photo, (620, 270), (620, 300), (255, 0, 0), thickness=3)
cv2.line(photo, (640, 270), (640, 300), (255, 0, 0), thickness=3)
cv2.line(photo, (560, 270), (580, 270), (0, 0, 255), thickness=3)
cv2.line(photo, (620, 270), (640, 270), (0, 0, 255), thickness=3)
# center of field
cv2.rectangle(photo, (0, 0), (photo.shape[1], photo.shape[0]), (255, 255, 255), thickness=3)
cv2.line(photo, (photo.shape[0], 0), (photo.shape[0], 220), (255, 255, 255), thickness=2)
cv2.line(photo, (photo.shape[0], 380), (photo.shape[0], photo.shape[1]), (255, 255, 255), thickness=2)
# line of goal left
cv2.line(photo, (0, 200), (150, 200), (255, 255, 255), thickness=2)
cv2.line(photo, (0, photo.shape[0] - 200), (150, photo.shape[0] - 200), (255, 255, 255), thickness=2)
cv2.line(photo, (150, 200), (150, photo.shape[0]-200), (255, 255, 255), thickness=2)
# line of goal right
cv2.line(photo, (photo.shape[1], 200), (photo.shape[1]-150, 200), (255, 255, 255), thickness=2)
cv2.line(photo, (photo.shape[1]-150, 200), (photo.shape[1]-150, photo.shape[0]-200), (255, 255, 255), thickness=2)
cv2.line(photo, (photo.shape[1]-150, photo.shape[0]-200), (photo.shape[1], photo.shape[0]-200), (255, 255, 255), thickness=2)
# angled
cv2.ellipse(img=photo, center=(5, 5), axes=(40, 40), angle=0., startAngle=0, endAngle=90, color=(255, 255, 255), thickness=2)
cv2.ellipse(img=photo, center=(photo.shape[1]-5, 5), axes=(40, 40), angle=90., startAngle=0, endAngle=90, color=(255, 255, 255), thickness=2)
cv2.ellipse(img=photo, center=(5, photo.shape[0]-5), axes=(40, 40), angle=270., startAngle=0, endAngle=90, color=(255, 255, 255), thickness=2)
cv2.ellipse(img=photo, center=(photo.shape[1]-5, photo.shape[0]-5), axes=(40, 40), angle=180., startAngle=0, endAngle=90, color=(255, 255, 255), thickness=2)

cv2.imshow('soccer field', photo)
cv2.waitKey(0)