import numpy as np 
import cv2
import imutils


class ImageDescriptor:
	def __init__(self,bins):
		self.bins = bins

	def describe(self, img):
		img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
		features = []

		(h, w) = image.shape[:2]
		(cX, cY) = (int(w * 0.5), int(h * 0.5))