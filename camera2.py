import cv2
import numpy as np
def getframe():  
	cap = cv2.VideoCapture(0)
	res,img=cap.read()
	res,img=cv2.imencode('.jpg', img) 
	return img.tobytes()
