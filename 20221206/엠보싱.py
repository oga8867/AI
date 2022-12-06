import cv2
import numpy as np

from utils import image_show

image_path = "./CM.jpg"
img = cv2.imread(image_path)

# 엠보싱 효과
filter1 = np.array([[0, 1, 0], [0, 0, 0], [0, -1, 0]])
filter2 = np.array([[-1, -1, 0], [-1, 0, 1], [0, 1, 1]])
emboss_img = cv2.filter2D(img, -1, filter2)
emboss_img = emboss_img + 128
image_show(emboss_img)
