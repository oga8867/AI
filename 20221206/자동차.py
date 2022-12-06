# 기본적인 이미지 처리 기술을 이용한 이미지 선명화 -1
import cv2
import numpy as np

img = cv2.imread('./car.jpg', 0)
print(img.shape)
img_rsize = cv2.resize(img, (640, 480))

blurred_1 = np.hstack([
    cv2.blur(img_rsize, (5, 5)),
    cv2.blur(img_rsize, (9, 9)),
    cv2.blur(img_rsize, (15, 15))
])

cv2.imshow("show", blurred_1)
cv2.waitKey(0)
