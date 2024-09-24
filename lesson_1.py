import  cv2
import numpy as np

photo = np.zeros ((450, 450, 3), dtype='uint8') # разрешение 450 на 450, 3 - три слоя цвета RGB
# RGB - стандарт
# BGR - формат в OpenCV
# photo[:] = 255, 0, 0  # 255 - максимально синий
photo[50:150, 100:100] = 255, 0, 255 # 50:150 - отступ по высоте, 100:100 -отступ по ширине
# создание квадрата
cv2.rectangle(photo, (0 ,0), (100, 100), (255, 0, 255), thickness=5)
# создание линии
cv2.line(photo, (10 ,10), (200, 200), (255, 0, 0), thickness=3)
cv2.line(photo,(0, photo.shape[0]//2), (photo.shape[1], photo.shape[0]//2), (0, 255, 0), thickness=3)
# создание окружности
cv2.circle(photo, (photo.shape[1]//2, photo.shape[0]//2), 100, (100, 100, 100), thickness=cv2.FILLED)
# вывод текстовых надписей
cv2.putText(photo, 'Urban', (100, 150), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255), 1)


cv2.imshow('Photo', photo)
cv2.waitKey(0) # 0 - бесконечный цикл ожидания, 999 - милисекунд


