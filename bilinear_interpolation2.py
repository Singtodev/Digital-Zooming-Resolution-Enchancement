import numpy as np
import cv2
from tkinter import Tk, filedialog

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
    new_height, new_width = int(height * zoom_factor), int(width * zoom_factor)

    # Create a grid of (x, y) coordinates in the zoomed image
    x = np.arange(new_width)
    y = np.arange(new_height)
    xv, yv = np.meshgrid(x, y)

    # Map the coordinates of the new image back to the original image
    x_orig = (xv + 0.5) / zoom_factor - 0.5
    y_orig = (yv + 0.5) / zoom_factor - 0.5

    # Find the nearest pixel coordinates in the original image
    x_low = np.floor(x_orig).astype(int)
    x_high = np.minimum(x_low + 1, width - 1)
    y_low = np.floor(y_orig).astype(int)
    y_high = np.minimum(y_low + 1, height - 1)

    # Calculate the bilinear interpolation weights
    x_weight = x_orig - x_low
    y_weight = y_orig - y_low

    # If the image is grayscale
    if len(image.shape) == 2:
        interpolated_pixel = (
            (1 - y_weight) * ((1 - x_weight) * image[y_low, x_low] + x_weight * image[y_low, x_high]) +
            y_weight * ((1 - x_weight) * image[y_high, x_low] + x_weight * image[y_high, x_high])
        ).astype(np.uint8)
        print("Gray Scale")
    # If the image is color
    elif len(image.shape) == 3:
        interpolated_pixel = np.zeros((new_height, new_width, image.shape[2]), dtype=np.uint8)
        for c in range(image.shape[2]):
            interpolated_pixel[:, :, c] = (
                (1 - y_weight) * ((1 - x_weight) * image[y_low, x_low, c] + x_weight * image[y_low, x_high, c]) +
                y_weight * ((1 - x_weight) * image[y_high, x_low, c] + x_weight * image[y_high, x_high, c])
            ).astype(np.uint8)
            
            print(interpolated_pixel)
        print("Color Image")
    else:
        raise ValueError("Unsupported image format. Expected 2D or 3D numpy array.")

    return interpolated_pixel

def browse_image():
    """
    Use Tkinter to open a file dialog for selecting an image file.

    Returns:
        str: File path of the selected image.
    """
    root = Tk()
    root.withdraw()  # Hide the Tkinter window
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")]
    )
    return file_path

# Load an image
image_path = browse_image()
if not image_path:
    print("No image selected.")
    exit()

image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    print(f"Error: Failed to load image '{image_path}'")
else:
    # Perform bilinear interpolation for zooming
    while True:
        zoom_factor = float(input('Enter Zoom Factor Value: '))  # Adjust this value to change the zoom level
        if zoom_factor > 0:
            break
        print('Zoom Factor Value Must More Than 0\nIf You Want To Zoom Out Use 0.X')
    zoomed_image = bilinear_interpolation(image, zoom_factor)

    # Display the zoomed image
    cv2.imshow('Original Image', image)
    cv2.imshow('Zoomed Image', zoomed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
