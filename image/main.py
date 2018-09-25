import numpy as np
import cv2
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

support = Polygon([(264,103),(517,172),(520,388),(262,397)])

ambient_height, ambient_width = new_ambient.shape[:2]
painting_height, painting_width = painting.shape[:2]
print ambient_height, ambient_width
print painting_height, painting_width

print painting[0,0]

for j in range(0, ambient_height - 1):
    for i in range(0, ambient_width - 1):
        #print support.contains(point)
        #new_ambient[i, j] = painting[i, j]
        point = Point(i, j)
        #print (i,j)
        new_ambient[j,i] = [255,255,255]
        if(support.contains(point)):
            new_ambient[j,i] = [0, 0, 0]

cv2.imshow('original ambient', ambient)
cv2.imshow('painting', painting)
cv2.imshow('new ambient', new_ambient)
cv2.waitKey(0)
cv2.destroyAllWindows()
