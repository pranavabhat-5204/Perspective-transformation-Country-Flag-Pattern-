import numpy as np
import streamlit as st
import cv2
from skimage import io
from matplotlib import pyplot as plt

# Load the images
img_flag = cv2.imread('/content/flag.png')  # Destination image
img_pattern = cv2.imread('/content/flagpattern.png') # Source image

plt.imshow(img_flag)
plt.imshow(img_pattern)

# Define the source and destination points for the homography
# These points represent corresponding points in both images
src_pts = np.float32([[0, 0], [img_pattern.shape[1], 0], [img_pattern.shape[1], img_pattern.shape[0]], [0, img_pattern.shape[0]]])
dst_pts = np.float32([[300, 70], [1035, 250], [1000, 800], [300, 700]])

# Calculate the homography matrix using RANSAC
H, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

warped_pattern = cv2.warpPerspective(img_pattern, H, (img_flag.shape[1], img_flag.shape[0]))
gray_warped_pattern = cv2.cvtColor(warped_pattern, cv2.COLOR_BGR2GRAY)
_, mask = cv2.threshold(gray_warped_pattern, 1, 255, cv2.THRESH_BINARY)
foreground = cv2.bitwise_and(warped_pattern, warped_pattern, mask=mask)
background = cv2.bitwise_and(img_flag, img_flag, mask=cv2.bitwise_not(mask))

# Combine foreground and background
result = cv2.add(foreground, background)
# Overlay the warped pattern onto the flag image
result = cv2.add(foreground, background)
result_rgb = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)


# Display the result
plt.imshow(result_rgb)
plt.show()
