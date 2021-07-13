#usr/bin/env python3
import numpy as np
import cv2
import pyautogui as gui
w=187
x=1
y=200
while True:
    if x > y and y < 4000:
        y += 120
        w += 2
    x+=1
    img = gui.screenshot(region = (68,370,w,100))
    img = cv2.cvtColor(np.array(img),cv2.COLOR_RGB2BGR)
    black = np.sum(img < 100)
    white = np.sum(img > 100)
    print("White: {} | Black: {} | X: {}".format(black,white,x))
    if black > 1350 and black < 30000:
        gui.press('up')
    if white > 1350 and white < 30000:
        gui.press('up')
    cv2.imshow('image',img)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break