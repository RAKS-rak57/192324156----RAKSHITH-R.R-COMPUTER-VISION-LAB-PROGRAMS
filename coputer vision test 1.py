import cv2

# Use double backslashes or a raw string to correctly format the path
image = cv2.imread(r"C:\Users\RAKSHITH.R.R\Downloads\DINESH.jpg")

if image is None:
    print("Error: Image not found at the specified path.")
else:
    cv2.imshow('Original', image)
    cv2.waitKey(0)

    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Grayscale', gray_image)
    cv2.waitKey(0)

    cv2.destroyAllWindows()
