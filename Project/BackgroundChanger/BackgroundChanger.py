import cv2
import cvzone
import os
from cvzone.SelfiSegmentationModule import SelfiSegmentation
from cvzone.FPS import FPS

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

listimg = os.listdir(r"C:\Users\TANISHQ\WALLPAPERS")
imglist = [cv2.imread(f"C:\\Users\\TANISHQ\\WALLPAPERS\\{imgpath}") for imgpath in listimg]

ind = 0
segmentor = SelfiSegmentation()
fpsReader = FPS()

while True:
    success, img = cap.read()
    if not success:
        break

    bgimg_resized = cv2.resize(imglist[ind], (img.shape[1], img.shape[0]))
    imgOut = segmentor.removeBG(img, bgimg_resized, cutThreshold=0.5)
    imgstack = cvzone.stackImages([img, imgOut], 2, 1)
    _, imgstack = fpsReader.update(imgstack, bgColor=(0, 0, 0), textColor=(255, 255, 255))
    
    cv2.imshow("Image", imgstack)
    
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('a'):
        ind = (ind + 1) % len(imglist)
    elif key == ord('d'):
        ind = (ind - 1) % len(imglist)

cap.release()
cv2.destroyAllWindows()
