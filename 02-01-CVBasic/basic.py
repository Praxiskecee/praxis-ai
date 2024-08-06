# Accesing opencv
import cv2
import imutils

image = cv2.imread("ganjar.jpeg")

# check image size
height,width,depth = image.shape
print("image size: ", height,width,depth)

# Show image
# cv2.imshow("Display", image)
# cv2.waitKey(0)

# resized = cv2.resize(image,(500, 500))
# cv2.imshow("Fixed Resizing", resized)
# cv2.waitKey(0)

# crop image
# cropped_image = image[50:300, 300:400]
# cv2.imshow("Cropped Image", cropped_image)
# cv2.waitKey(0)

# Rotating an image
# rotated = imutils.rotate(image, -180)
# cv2.imshow("Imutils Rotation", rotated)
# cv2.waitKey(0)

# blur image
# blurred = cv2.GaussianBlur(image, (25, 25), 0)
# cv2.imshow("Blurred", blurred)
# cv2.waitKey(0)

# drawing
# output = image.copy()
# cv2.rectangle(output, (230, 100), (500, 550), (255, 0, 255), 4)
# cv2.imshow("Rectangle", output)
# cv2.waitKey(0)

# drawing 
output = image.copy()
cv2.circle(output, (370, 320), 210, (255, 0, 0), 4)
cv2.imshow("Circle", output)
cv2.waitKey(0)

# drawing
# output = image.copy()
# cv2.line(output, (180, 50), (500, 600), (0, 0, 255), 5)
# cv2.line(output, (600, 50), (200, 600), (0, 0, 255), 5)
# cv2.imshow("Line", output)
# cv2.waitKey(0)

# Text 
# output = image.copy()
# cv2.putText(output, "pak ganjar say : wong saya suka kok", (10, 25), 
# 	cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
# cv2.imshow("Text", output)
# cv2.waitKey(0)