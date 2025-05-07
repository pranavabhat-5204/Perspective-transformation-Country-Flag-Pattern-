import numpy as np
import streamlit as st
import cv2
from skimage import io
from matplotlib import pyplot as plt


st.title("Image Warping App")
uploaded_flag = st.file_uploader("Upload Flag Image", type=["jpg", "png", "jpeg"])
uploaded_pattern = st.file_uploader("Upload Pattern Image", type=["jpg", "png", "jpeg"])

if uploaded_flag and uploaded_pattern:
  img_flag = cv2.imread('/content/flag.png')  # Destination image
  img_pattern = cv2.imread('/content/pattern.png') # Source image

  plt.imshow(img_flag)
  plt.imshow(img_pattern)


  sor_pts = np.float32([[0, 0], [img_pattern.shape[1], 0], [img_pattern.shape[1], img_pattern.shape[0]], [0, img_pattern.shape[0]]])
  dest_pts = np.float32([[300, 70], [1035, 250], [1000, 800], [300, 700]])

  matrix = cv2.getPerspectiveTransform(sor_pts, dest_pts)

  warped_pattern = cv2.warpPerspective(img_pattern, matrix, (img_flag.shape[1], img_flag.shape[0]))

  gray_warped_pattern = cv2.cvtColor(warped_pattern, cv2.COLOR_BGR2GRAY)
  _, mask = cv2.threshold(gray_warped_pattern, 1, 255, cv2.THRESH_BINARY)
  pattern = cv2.bitwise_and(warped_pattern, warped_pattern, mask=mask)
  flag = cv2.bitwise_and(img_flag, img_flag, mask=cv2.bitwise_not(mask))

  result = cv2.add(pattern, flag)
  result = cv2.add(pattern, flag)
  result_color = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)


  # Display the result
  st.image(result_color, caption="Warped Image", use_column_width=True)
