#importing the libraries
import numpy as np
import cv2
from skimage import io
from matplotlib import pyplot as plt


img_flag = cv2.imread('/content/flag.png')  # image to which the patter has to be transformed
img_pattern = cv2.imread('/content/pattern.png') # pattern image

#finding the coordinates of the images from the plot
plt.imshow(img_flag)
plt.imshow(img_pattern)

#including the coordinates which we have found out
sor_pts = np.float32([[0, 0], [img_pattern.shape[1], 0], [img_pattern.shape[1], img_pattern.shape[0]], [0, img_pattern.shape[0]]])
dest_pts = np.float32([[300, 70], [1035, 250], [1000, 800], [300, 700]])

#getting the matrix
matrix = cv2.getPerspectiveTransform(sor_pts, dest_pts)

#here I used the grey wrapping to improve the isolation for the flag from the background
warped_pattern = cv2.warpPerspective(img_pattern, matrix, (img_flag.shape[1], img_flag.shape[0]))
gray_warped_pattern = cv2.cvtColor(warped_pattern, cv2.COLOR_BGR2GRAY)
_, mask = cv2.threshold(gray_warped_pattern, 1, 255, cv2.THRESH_BINARY)
pattern = cv2.bitwise_and(warped_pattern, warped_pattern, mask=mask)
flag = cv2.bitwise_and(img_flag, img_flag, mask=cv2.bitwise_not(mask))

#getting the resulting image
result = cv2.add(pattern, flag)
result = cv2.add(pattern, flag)
result_color = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
plt.imshow(result_color)

# I have provided my approach and error handling in the readme file. I have also implement a docker application of the same on Hugginface
