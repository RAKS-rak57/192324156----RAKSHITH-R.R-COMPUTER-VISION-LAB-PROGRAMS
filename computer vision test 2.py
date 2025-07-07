import cv2

# Use raw string format to prevent path issues
image_path = r"C:\Users\RAKSHITH.R.R\OneDrive\Desktop\ML DATSET EYE DISEASE\normal\8_left.jpg"
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found at the specified path.")
else:
    # Convert image to grayscale for edge detection
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    edges = cv2.Canny(gray_image, threshold1=100, threshold2=200)

    # Display the results
    cv2.imshow('Canny Edge Detection', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
