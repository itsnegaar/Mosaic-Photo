#create photomosaic from input images


# importing packages
from compileall import compile_dir
from importlib.resources import path
from re import X
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from skimage import data
from skimage import exposure
from skimage.exposure import match_histograms
import random

  
#read a random path form the file
def rand(filename):
	lines = open(filename).read().splitlines()
	return random.choice(lines)


#forgroundimage
add = input('insert the picture\'s address: ')
forimg = cv.imread(add)
forimg= cv.resize(forimg, (1280,720))
# #devide picture to n*m pieces
n = 50
m = 50
#find forground width and height
W = forimg.shape[1]
H = forimg.shape[0]
#size of each patch
h = int(H/n)
w = int(W/m)
dim = (w,h)
# print(h,w)
# print(forimg.shape)
# exit()

for i in range(H):
    for j in range(W):
        #choose and read a random photo
        path = rand('/home/veunex/a/mosaicpics/test.txt')
        img = cv.imread(path)
        # print(img.shape)
        #resize the chosen image
        # resizedImage = cv.resize(img, dim, interpolation = cv.INTER_AREA)

        #define a aprt of foreground image as the refrence
        x = i*h
        xp = (i+1)*h
        y = j*w
        yp = (j+1)*w
        # print(x, xp, y, yp)
        reference = forimg[x:xp,y:yp]
        if xp > H or yp > W:
            continue
        h_r, w_r,_ = reference.shape
        
        # print(h_r, w_r)
        resizedImage = cv.resize(img, (w_r,h_r), interpolation = cv.INTER_AREA)


        # print(reference.shape, resizedImage.shape)
        #match the refrence with the chosen pic 
        matchedimage = match_histograms(resizedImage , reference ,channel_axis = True)


        #replace the patch with final image
        forimg[x:xp,y:yp] = matchedimage 

    
cv.imshow('final',forimg)
cv.waitKey(0)