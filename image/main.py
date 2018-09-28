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

#transformation = np.array([ [0.8714, -0.0199, 264],
#                            [0.2598,  0.6926, 103],
#                            [0.0007, -0.0001, 1]])

#P1 = (103,264)
#P2 = (172,517)
#P3 = (397,262) 
#P4 = (388,520)
P1 = (140,291)
P2 = (188,497)
P3 = (361,289) 
P4 = (360,499)
support = Polygon([P1, P2, P3, P4])
painting_polygon = Polygon([(0,0),(0,504),(411,0),(411,504)])

#Finding transformation matrix:
support_coords = list(support.exterior.coords)
painting_coords = list(painting_polygon.exterior.coords)

c = support_coords[0][0]
f = support_coords[0][1]
i = 1

multFac1 = support_coords[2][0] - support_coords[3][0]
multFac2 = support_coords[2][1] - support_coords[3][1]
y = ( multFac1*( support_coords[0][1] - support_coords[3][1]) - multFac2*( support_coords[0][0] - support_coords[3][0] ))/(multFac1*( support_coords[1][1] - support_coords[3][1] ) - multFac2*( support_coords[1][0] - support_coords[3][0] ))
x = (( support_coords[0][0] - support_coords[3][0] ) - ( support_coords[1][0] - support_coords[3][0] )*y )/multFac1

a = (support_coords[2][0]*x - support_coords[0][0])/painting_coords[3][0]
d = (support_coords[2][1]*x - support_coords[0][1])/painting_coords[3][0]
g = (x - 1)/painting_coords[3][0]

b = (support_coords[1][0]*y - support_coords[0][0])/painting_coords[3][1]
e = (support_coords[1][1]*y - support_coords[0][1])/painting_coords[3][1]
h = (y - 1)/painting_coords[3][1]

transformation = np.array([[a, b, c],
                           [d, e, f],
                           [g, h, i]])

print transformation

print 'testing the transformation'
m,n,o = np.matmul(transformation, np.array([[0],[0],[1]]))
print(m/o, n/o)

m,n,o = np.matmul(transformation, np.array([[411],[0],[1]]))
print(m/o, n/o)

m,n,o = np.matmul(transformation, np.array([[0],[504],[1]]))
print(m/o, n/o)

m,n,o = np.matmul(transformation, np.array([[411],[504],[1]]))
print(m/o, n/o)

inverse = np.linalg.inv(transformation)
print inverse

multiplication = np.matmul(transformation, inverse)
print multiplication




#declaring support quadril
support = Polygon([P1, P2, P4, P3])

ambient_height, ambient_width = new_ambient.shape[:2]
painting_height, painting_width = painting.shape[:2]
print ambient_height, ambient_width
print painting_height, painting_width

print painting[0,0]

for j in range(0, ambient_height - 1):
    for i in range(0, ambient_width - 1):
        #print support.contains(point)
#        #new_ambient[i, j] = painting[i, j]
         point1 = Point(j, i)
#        #print (i,j)
#        #new_ambient[j,i] = [255,255,255]
         correspondent = np.matmul(inverse, [j, i, 1])
#        #print correspondent
         point = Point(correspondent[1]/correspondent[2], correspondent[0]/correspondent[2])
         if(support.contains(point1)):
#            #print point
#            #print math.floor(point.x), math.floor(point.y)
             x = int(math.floor(point.x))
             y = int(math.floor(point.y))
             #if(x < 0):
             #    x = 0
             #elif x > 504:
             #    x = 504
             #if y < 0:
             #    y = 0
             #elif y > 411:
             #    y = 411
            #print x, y
             new_ambient[j,i] = painting[y, x] 
#            new_ambient[j,i] = 0
#
cv2.imshow('original ambient', ambient)
cv2.imshow('painting', painting)
cv2.imshow('new ambient', new_ambient)
cv2.waitKey(0)
cv2.destroyAllWindows()
