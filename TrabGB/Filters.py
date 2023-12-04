import numpy as np
import cv2 as cv

def apply_all(imgOriginal):
	imgBNW = imgOriginal.copy()
	imgColored = imgOriginal.copy()
	imgNeg = imgOriginal.copy()
	imgGrey = cv.cvtColor(imgOriginal,cv.COLOR_BGR2GRAY)
	imgBin = imgGrey.copy()
	imgCanny = cv.Canny(cv.blur(imgOriginal,(5,5)),50,100)
	imgVig = imgOriginal.copy()
	imgColorRamp = imgOriginal.copy()
	imgMotionBlur = imgOriginal.copy()
	imgA3 = imgOriginal.copy()
	imgA4 = imgOriginal.copy()
	imgA5 = imgOriginal.copy()
		
	rows, cols = imgVig.shape[:2] 
	x = cv.getGaussianKernel(cols,200) 
	y = cv.getGaussianKernel(rows,200)
	result = y * x.T 
	mask = 255 * result / np.linalg.norm(result) 
	imgVig = np.copy(imgVig) 
		
	for i in range(3): 
		imgVig[:,:,i] = imgVig[:,:,i] * mask 

	modifyingColor = [0, 255, 0] #modifica a cor para verde, mas alterar depois para ter os 3 filtros
	modifyingColorA3 = [200, 50, 100]

	k = 150

	# implementando motionblur
	motionBlur = np.zeros((15,15))
	motionBlur[7, :] = np.ones(15)
	motionBlur = motionBlur / 15
	# aplicando motionblur
	imgMotionBlur = cv.filter2D(imgOriginal, -1, motionBlur)

	for i in range(imgOriginal.shape[0]): #percorre linhas
		for j in range(imgOriginal.shape[1]): #percorre colunas

			mediaPond = imgOriginal.item(i,j,0) * 0.07 + imgOriginal.item(i,j,1) * 0.71 + imgOriginal.item(i,j,2) * 0.21
			imgBNW.itemset((i,j,0),mediaPond) # canal B
			imgBNW.itemset((i,j,1),mediaPond) # canal G
			imgBNW.itemset((i,j,2),mediaPond) # canal R

			blue = imgOriginal.item(i,j,0) | modifyingColor[0]
			green = imgOriginal.item(i,j,1) | modifyingColor[1]
			red = imgOriginal.item(i,j,2) | modifyingColor[2]

			imgColored.itemset((i,j,0),blue) 
			imgColored.itemset((i,j,1),green)
			imgColored.itemset((i,j,2),red) 

			imgNeg.itemset((i,j,0),imgNeg.item(i,j,0)^255) # canal B
			imgNeg.itemset((i,j,1),imgNeg.item(i,j,1)^255) # canal G
			imgNeg.itemset((i,j,2),imgNeg.item(i,j,2)^255) # canal R

			if imgGrey.item(i,j) < k:
				imgBin.itemset((i,j),0)
			else:
				imgBin.itemset((i,j),255)

			if imgGrey.item(i,j) < 100:
				imgColorRamp.itemset((i,j,0),255)
				imgColorRamp.itemset((i,j,1),255)
				imgColorRamp.itemset((i,j,2),0)
			elif imgGrey.item(i,j) < 150:
				imgColorRamp.itemset((i,j,0),255)
				imgColorRamp.itemset((i,j,1),0)
				imgColorRamp.itemset((i,j,2),255)
			else:
				imgColorRamp.itemset((i,j,0),0)
				imgColorRamp.itemset((i,j,1),255)
				imgColorRamp.itemset((i,j,2),255)

			if imgGrey.item(i,j) < 50:
				imgA5.itemset((i,j,0),50)
				imgA5.itemset((i,j,1),50)
				imgA5.itemset((i,j,2),0)

			if imgGrey.item(i,j) < 50:
				gamma = (imgGrey.item(i,j)/255)**3
				imgA4.itemset((i,j,0),gamma)
				imgA4.itemset((i,j,1),gamma)
				imgA4.itemset((i,j,2),gamma)

			blue = imgOriginal.item(i,j,0) | modifyingColorA3[0]
			green = imgOriginal.item(i,j,1) | modifyingColorA3[1]
			red = imgOriginal.item(i,j,2) | modifyingColorA3[2]

			imgA3.itemset((i,j,0),blue) 
			imgA3.itemset((i,j,1),green)
			imgA3.itemset((i,j,2),red) 
			
	return {
		"Original": imgOriginal,
		"BlackAndWhite": imgBNW,
		"Colored": imgColored,
		"Negative": imgNeg,
		"Binary": imgBin,
		"Canny": imgCanny,
		"Vignette": imgVig, 
		"ColorRamp": imgColorRamp,
		"MotionBlur": imgMotionBlur,
		"A5": imgA5,
		"A4": imgA4,
		"A3": imgA3
	}