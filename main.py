import numpy as np 
import cv2 
import pyautogui

image = pyautogui.screenshot()
# if you are using linux run sudo apt-get install scrot
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR) 
# author = 'Jayson'
cv2.imwrite("image1.png", image)
