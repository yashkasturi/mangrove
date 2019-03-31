import cv2
import numpy as np
from skimage.io import imread

def main():

	a=0
	b=0

	def af():
		lowerBound=np.array([55,60,0])
		upperBound=np.array([90,200,255])
		cam= cv2.imread('19-12-18.JPg')
		img=cv2.resize(cam,(340,220))
		imgHSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
		mask=cv2.inRange(imgHSV,lowerBound,upperBound)
		imgHSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
		mask=cv2.inRange(imgHSV,lowerBound,upperBound)
		ratio_white = cv2.countNonZero(mask)/(img.size/3)
		a=np.round(ratio_white*100, 2)
		#print('Mangrove percentage(Before):', np.round(ratio_white*100, 2))
	    #cv2.imshow("mask",mask)
		#cv2.imshow("cam1",img)
		#cv2.imwrite("after.jpg",mask)
		#cv2.waitKey(80)
		return str(a)

	def bf():
		
		lowerBound=np.array([55,60,0])
		upperBound=np.array([90,200,255])
		cam= cv2.imread('19-12-18.JPg')
		img=cv2.resize(cam,(340,220))
		imgHSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
		mask=cv2.inRange(imgHSV,lowerBound,upperBound)
		ratio_white = cv2.countNonZero(mask)/(img.size/3)
		b=np.round(ratio_white*100, 2)
		print('Mangrove percentage(After):', np.round(ratio_white*100, 2))
		cv2.imshow("mask",mask)
		cv2.imshow("cam1",img)
		cv2.imwrite("before.jpg",mask)
		#cv2.waitKey(10)
		return str(b)
		#yield cv2.imencode('.jpg',mask)[1].tobytes()
	 
	def diff():

		c=a-b
		return str(c)
		#print(a-b)
		#print('Mangrove percentage difference:',a-b)
     
     
	af()
	bf()
	diff()

#main()

if __name__=='__main__':
    
	print(main())