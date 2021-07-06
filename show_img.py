import matplotlib.pyplot as plt
import cv2
def show_img(img):
  plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
  plt.show()
