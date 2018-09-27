import numpy as np
import cv2
import math
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

ambient = cv2.imread('ambient.jpg', 1)
ambient = cv2.resize(ambient, (0,0), fx=0.25, fy=0.25)
new_ambient = ambient.copy()

painting = cv2.imread('painting.jpg',1)
painting = cv2.resize(painting, (0,0), fx=0.5, fy=0.5)

transformation = np.array([ [0.8714, -0.0199, 264],
                            [0.2598,  0.6926, 103],
                            [0.0007, -0.0001, 1]])

print transformation
inverse = np.linalg.inv(transformation)
print inverse

multiplication = np.matmul(transformation, inverse)
print multiplication

support = Polygon([(103,264),(172,517),(388,520),(397,262)])

ambient_height, ambient_width = new_ambient.shape[:2]
painting_height, painting_width = painting.shape[:2]
print ambient_height, ambient_width
print painting_height, painting_width

print painting[0,0]

for j in range(0, ambient_height - 1):
    for i in range(0, ambient_width - 1):
        #print support.contains(point)
        #new_ambient[i, j] = painting[i, j]
        point1 = Point(j, i)
        #print (i,j)
        #new_ambient[j,i] = [255,255,255]
        correspondent = np.matmul(inverse, [j, i, 1])
        #print correspondent
        point = Point(correspondent[1]/correspondent[2], correspondent[0]/correspondent[2])
        if(support.contains(point1)):
            #print point
            print math.floor(point.x), math.floor(point.y)
            x = int(math.floor(point.x)) - 242
            y = int(math.floor(point.y)) + 214
            if(x < 0):
                x = 0
            elif x > 504:
                x = 504
            if y < 0:
                y = 0
            elif y > 411:
                y = 411
            print x, y
            new_ambient[j,i] = painting[y, x] 

cv2.imshow('original ambient', ambient)
cv2.imshow('painting', painting)
cv2.imshow('new ambient', new_ambient)
cv2.waitKey(0)
cv2.destroyAllWindows()
