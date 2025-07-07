import cv2
image = cv2.imread(r"C:\Users\RAKSHITH.R.R\OneDrive\Desktop\computer vision test 3-1.jpg")
k_size = (5, 5)  
sigma_x = 0    
blurred_image = cv2.GaussianBlur(image, k_size, sigma_x)
cv2.imwrite('blurred_image.jpg', blurred_image)
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
