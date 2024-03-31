import numpy as np
import cv2
from tkinter import filedialog
def bilinear_interpolation(image, zoom_factor):
    """
    Performs bilinear interpolation on an image for digital zooming.
    
    Args:
        image (numpy.ndarray): Input image as a 2D or 3D numpy array.
        zoom_factor (float): Zoom factor for upscaling the image.
        
    Returns:
        numpy.ndarray: Zoomed image as a 2D or 3D numpy array.
    """
    # Get the dimensions of the input image
    height, width = image.shape[:2]
    
    # Calculate the new dimensions of the zoomed image
    new_height = int(height * zoom_factor)
    new_width = int(width * zoom_factor)
    
    # Create a new blank image with the zoomed dimensions
    zoomed_image = np.zeros((new_height, new_width, image.shape[2]), dtype=image.dtype)
    
    # Perform bilinear interpolation
    for y in range(new_height):
        for x in range(new_width):
            # Map the coordinates of the new image back to the original image
            x_orig = (x + 0.5) / zoom_factor - 0.5
            y_orig = (y + 0.5) / zoom_factor - 0.5
            
            # Find the nearest pixel coordinates in the original image
            x_low = int(np.floor(x_orig))
            x_high = min(x_low + 1, width - 1)
            y_low = int(np.floor(y_orig))
            y_high = min(y_low + 1, height - 1)
            
            # Calculate the bilinear interpolation weights
            x_weight = x_orig - x_low
            y_weight = y_orig - y_low
            
            # Perform bilinear interpolation
            zoomed_image[y, x] = (
                (1 - y_weight) * (
                    (1 - x_weight) * image[y_low, x_low] + x_weight * image[y_low, x_high]
                ) + y_weight * (
                    (1 - x_weight) * image[y_high, x_low] + x_weight * image[y_high, x_high]
                )
            )
    
    return zoomed_image

def browseImage():
    return filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
# Load an image
image = cv2.imread(browseImage())

# Perform bilinear interpolation for zooming
zoom_factor = 2.0  # Adjust this value to change the zoom level
zoomed_image = bilinear_interpolation(image, zoom_factor)

# Display the zoomed image
cv2.imshow('Zoomed Image', zoomed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()