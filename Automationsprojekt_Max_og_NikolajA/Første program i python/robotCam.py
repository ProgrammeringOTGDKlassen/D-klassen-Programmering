import cv2


#import numpy as np

class RobotCam():

	def __init__(self):
		self.vc = cv2.VideoCapture(1)
		self.threshold_value = 95
		self.min_area = 400
		self.max_area = 20000
		self.match_score = 0.17
		self.frame = None
		self.show_image = True
		#cv2.namedWindow("results")		
		if self.vc.isOpened():
			print('Forbindelse til kamera er oprettet.')
			rval, self.frame = self.vc.read()
			#cv2.imshow("results", self.frame)

	def show(self):
		self.analyze(silent=True)
		#cv2.imshow("results", self.frame)

	def analyze(self, silent=False):
		rect = None
		cx = None
		cy = None
		if not silent:
			print('Analyserer billede...')
		if self.vc.isOpened():
			rval, self.frame = self.vc.read()
			cv2.imwrite("./original.jpg", self.frame)
		
			src_gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
			ret, dst = cv2.threshold(src_gray, self.threshold_value, 255, 0)
			cv2.imwrite("./threshold.jpg", dst)
			image, contours, hierarchy = cv2.findContours(dst, 1, 2)

			sorted_contours = []
			#cv2.imshow("preview", image)

			#Sorter på størrelvse:
			for c in contours:
				area = cv2.contourArea(c)
				if self.min_area < area < self.max_area:
					#cv2.drawContours(self.frame,c,-1,(255,0,0),3)
					sorted_contours.append(c)

			#Sorter på elongatedness
			#Da vi kigger efter rektangler
			# kan vi bruge højde/bredde som 
			# mål for elongatedness:
			# https://user.engineering.uiowa.edu/~dip/lecture/Shape3.html
			i = 0
			tmp = cv2.imread('reference.jpg',cv2.IMREAD_COLOR)

			reference = cv2.cvtColor(tmp, cv2.COLOR_BGR2GRAY)
			ret, dst = cv2.threshold(reference, self.threshold_value, 255, 0)
			ref_img, ref_cnt, hierarchy = cv2.findContours(dst, 1, 2)
				
			for c in sorted_contours:
				rect = cv2.minAreaRect(c)
				boxf = cv2.boxPoints(rect)
				#box = np.int0(boxf)
				

				M = cv2.moments(c)
				hu = cv2.HuMoments(M)
				cx = M['m10']/M['m00']
				cy = M['m01']/M['m00']

				#Tegner en firkant ved cx,cy
				#Bemærk: y,x ikke x,y
				#self.frame[int(cy)-5:int(cy)+5,int(cx)-5:int(cx)+5] = (0,0,(255/len(sorted_contours))*(i+1))

				i += 1

				#Calculate match score:
				# Metode 1 synes at være den bedste.
				score = cv2.matchShapes(ref_cnt[0], c, 1, 0.0)
				
				if score < self.match_score:
					if not silent:
						print('Der er fundet en klods ved ({:5f},{:5f}), i en vinkel på {:5f} grader. Score: {}'.format(cx,cy, rect[2], score))
					#cv2.drawContours(self.frame,[box],0,(0,0,255),2)
					#Vis text
					cv2.putText(self.frame, "({},{}), Vinkel: {}".format(int(cx),int(cy), rect[2]), (int(cx), int(cy)), cv2.FONT_HERSHEY_COMPLEX_SMALL , 0.5, 2)
			
			#if self.show_image:
				#cv2.imshow("results", self.frame)
			if not silent:
				print('Analyse færdig.')
			return cx, cy, rect[2]
'''
rc = RobotCam()
rc.show_image = True
cont = True
while cont:
	key = cv2.waitKey(20)
	key = int(key) % 256
	if key != -1 and key != 255:
		print(key)
	if key == ord('a'):
		rc.analyze()
	if key == ord('v'):
		rc.show()
	if key == ord('s'):
		print("saving")
		cv2.imwrite("./webcam_photo.jpg", rc.frame)
		print("done saving")
		#break
	if key == 27:
		cont = False
		#break

	

def takePicture():
	cv2.namedWindow("preview")
	print('1')
	vc = cv2.VideoCapture(1)
	print('2')
	threshold_value = 100
	if vc.isOpened():
		rval, frame = vc.read()
		#for i in range(0,100):
			#print(i,vc.get(i))
	else:
		rval = False
	cv2.createTrackbar('THR', "preview" , 0, 255, dome)
	cv2.createTrackbar('TYPE', "preview" , 0, 4, dome)
	
	while rval:
		threshold_value = cv2.getTrackbarPos("THR", "preview")
		types = cv2.getTrackbarPos("TYPE", "preview")
		src_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		ret, dst = cv2.threshold(src_gray, threshold_value, 255, types)

		image, contours, hierarchy = cv2.findContours(dst, 1, 2)
		cs = []
		for c in contours:
			if len(c) > 300:
				cs.append(c)

		#if len(cs)>0:
			#print(len(cs))
			#image = cv2.drawContours(image, cs, -1, (255,0,0), cv2.FILLED)

		
		cv2.imshow("preview", image)



		#cv2.imshow("preview", frame)
		rval, frame = vc.read()
		key = cv2.waitKey(20)
		if str(key) != '-1':
			print(key)
		if key == 32:
			rval, frame = vc.read()
		if key == 115:
			print("saving")
			cv2.imwrite("../images/temp/webcam_photo.jpg", frame)
			print("done saving")
			#break
		if key == 27:
			break

	cv2.destroyWindow("preview")
#takePicture()




#Uden kamera:
def analyze_image():
	cv2.namedWindow("contours")
	frame = cv2.imread('webcam_photo.jpg',cv2.IMREAD_COLOR)
	threshold_value = 95
	src_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	ret, dst = cv2.threshold(src_gray, threshold_value, 255, 0)
	image, contours, hierarchy = cv2.findContours(dst, 1, 2)

	sorted_contours = []
	#cv2.imshow("preview", image)

	#Sorter på størrelse:
	for c in contours:
		area = cv2.contourArea(c)
		if 400 < area < 10000:			
			cv2.drawContours(frame,c,-1,(255,0,0),3)
			sorted_contours.append(c)

	#Sorter på elongatedness
	#Da vi kigger efter rektangler
	# kan vi bruge højde/bredde som 
	# mål for elongatedness.cv2.imwrite("../images/temp/webcam_photo.jpg", frame)
	# https://user.engineering.uiowa.edu/~dip/lecture/Shape3.html
	i = 0
	tmp = cv2.imread('reference.jpg',cv2.IMREAD_COLOR)

	reference = cv2.cvtColor(tmp, cv2.COLOR_BGR2GRAY)
	ret, dst = cv2.threshold(reference, threshold_value, 255, 0)
	ref_img, ref_cnt, hierarchy = cv2.findContours(dst, 1, 2)
	#cv2.imshow("reference", ref_img)	
	for c in sorted_contours:
		rect = cv2.minAreaRect(c)
		box = cv2.boxPoints(rect)
		box = np.int0(box)
		

		M = cv2.moments(c)
		hu = cv2.HuMoments(M)
		cx = M['m10']/M['m00']
		cy = M['m01']/M['m00']

		#Tegner en firkant ved cx,cy
		#Bemærk: y,x ikke x,y
		#frame[int(cy)-5:int(cy)+5,int(cx)-5:int(cx)+5] = (0,0,(255/len(sorted_contours))*(i+1))

		
		i += 1

		#Calculate match score:
		# Metode 1 synes at være den bedste.
		score1 = cv2.matchShapes(ref_cnt[0], c, 1, 0.0)
		
		print('Scores: {}'.format(score1))
		if score1 < 0.3:
			print('Match ved ({},{})!'.format(cx,cy))
			cv2.drawContours(frame,[box],0,(0,0,255),2)
			#Vis text
			cv2.putText(frame, "Blob: " + str(i), (int(cx), int(cy)), cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
	cv2.imshow("contours", frame)

	rval = True
	while rval:
		key = cv2.waitKey(20)
		if key == 27:
			rval = False

#Uden kamera:
def analyze_camera_img():
	vc = cv2.VideoCapture(1)
	threshold_value = 95	
	if vc.isOpened():
		rval, frame = vc.read()

	cv2.namedWindow("contours")
	
	src_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	ret, dst = cv2.threshold(src_gray, threshold_value, 255, 0)
	image, contours, hierarchy = cv2.findContours(dst, 1, 2)

	sorted_contours = []
	#cv2.imshow("preview", image)

	#Sorter på størrelse:
	for c in contours:
		area = cv2.contourArea(c)
		if 400 < area < 10000:			
			cv2.drawContours(frame,c,-1,(255,0,0),3)
			sorted_contours.append(c)

	#Sorter på elongatedness
	#Da vi kigger efter rektangler
	# kan vi bruge højde/bredde som 
	# mål for elongatedness.cv2.imwrite("../images/temp/webcam_photo.jpg", frame)
	# https://user.engineering.uiowa.edu/~dip/lecture/Shape3.html
	i = 0
	tmp = cv2.imread('reference.jpg',cv2.IMREAD_COLOR)

	reference = cv2.cvtColor(tmp, cv2.COLOR_BGR2GRAY)
	ret, dst = cv2.threshold(reference, threshold_value, 255, 0)
	ref_img, ref_cnt, hierarchy = cv2.findContours(dst, 1, 2)
	#cv2.imshow("reference", ref_img)	
	for c in sorted_contours:
		rect = cv2.minAreaRect(c)
		box = cv2.boxPoints(rect)
		box = np.int0(box)
		

		M = cv2.moments(c)
		hu = cv2.HuMoments(M)
		cx = M['m10']/M['m00']
		cy = M['m01']/M['m00']

		#Tegner en firkant ved cx,cy
		#Bemærk: y,x ikke x,y
		#frame[int(cy)-5:int(cy)+5,int(cx)-5:int(cx)+5] = (0,0,(255/len(sorted_contours))*(i+1))

		
		i += 1

		#Calculate match score:
		# Metode 1 synes at være den bedste.
		score1 = cv2.matchShapes(ref_cnt[0], c, 1, 0.0)
		
		print('Scores: {}'.format(score1))
		if score1 < 0.3:
			print('Match ved ({},{})!'.format(cx,cy))
			cv2.drawContours(frame,[box],0,(0,0,255),2)
			#Vis text
			cv2.putText(frame, "Blob: " + str(i), (int(cx), int(cy)), cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
	cv2.imshow("contours", frame)

	rval = True
	while rval:
		key = cv2.waitKey(20)
		if key == 27:
			rval = False

analyze_camera_img()'''