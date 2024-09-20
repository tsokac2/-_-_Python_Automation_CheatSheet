import cv2

color = cv2.imread('galaxy.jpeg',0)
# print(type(color))
cv2.imwrite('galaxy-grey.jpeg', color)