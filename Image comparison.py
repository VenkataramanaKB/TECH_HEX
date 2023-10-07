import cv2
from skimage import io
from skimage.metrics import structural_similarity as ssim

print("Comparing images of various Empty Wagon")

#Input images are given manually
input_image1 = io.imread('Empty_Input1.PNG')
input_image2 = io.imread('Empty_Input2.PNG')

# A filter image is given which is used for reference
filter_image1 = io.imread('Empty_Filter.PNG')

input_image_gray1 = cv2.cvtColor(input_image1, cv2.COLOR_BGR2GRAY)
input_image_gray2 = cv2.cvtColor(input_image2, cv2.COLOR_BGR2GRAY)
filter_image_gray1 = cv2.cvtColor(filter_image1, cv2.COLOR_BGR2GRAY)

# Structural Similarity is compared between input image and filter image
ssim_score1 = ssim(input_image_gray1, filter_image_gray1)

threshold = 0.9

if ssim_score1 > threshold:
    print("The wagon is completely empty")
else:
    print("The wagon is not empty")


# Structural Similarity is compared between input image and filter image
ssim_score2 = ssim(input_image_gray2, filter_image_gray1)

if ssim_score2 > threshold:
    print("The wagon is completely empty")
else:
    print("The wagon is not empty")

print("Comparing images of various filled wagons")

#Input images are given manually
input_image3 = io.imread('Filled_Input1.PNG')
input_image4 = io.imread('Filled_Input2.PNG')

# A filter image is given which is used for reference
filter_image1 = io.imread('Filled_Filter.PNG')

input_image_gray3 = cv2.cvtColor(input_image3, cv2.COLOR_BGR2GRAY)
input_image_gray4 = cv2.cvtColor(input_image4, cv2.COLOR_BGR2GRAY)
filter_image_gray2 = cv2.cvtColor(filter_image1, cv2.COLOR_BGR2GRAY)

# Structural Similarity is compared between input image and filter image
ssim_score3 = ssim(input_image_gray3, filter_image_gray2)

if ssim_score3 > threshold:
    print("The wagon is completely filled")
else:
    print("The wagon is not filled completely")


# Structural Similarity is compared between input image and filter image
ssim_score4 = ssim(input_image_gray4, filter_image_gray2)

if ssim_score4 > threshold:
    print("The wagon is completely filled")
else:
    print("The wagon is not filled completely")