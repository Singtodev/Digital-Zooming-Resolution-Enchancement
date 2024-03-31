import cv2
from tkinter import Tk, filedialog

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
    zoom_factor = 2.0  # Adjust this value to change the zoom level
    new_height, new_width = int(image.shape[0] * zoom_factor), int(image.shape[1] * zoom_factor)
    zoomed_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

    # Display the zoomed image
    cv2.imshow('Original Image', image)
    cv2.imshow('Zoomed Image', zoomed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
