from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np

# Load the given image
input_path = 'assignment-001-given.jpg'
output_path = 'assignment-001-result.jpg'

# Load the image using OpenCV
image = cv2.imread(input_path)

# Define the bounding box for the license plate
bbox = (180, 200, 1000, 910) 

# Draw the green rectangle for bounding box
start_point = (bbox[0], bbox[1])
end_point = (bbox[2], bbox[3])
color = (0, 255, 0)  # Green color
thickness = 4
cv2.rectangle(image, start_point, end_point, color, thickness)

# Define text properties
text = "RAH972U"
font_scale = 1.5
font_color = (0, 255, 0)  # Green
font = cv2.FONT_HERSHEY_SIMPLEX
font_thickness = 3

# Get text size for positioning
text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
text_x = bbox[0]  # Align text with the left edge of the bounding box
text_y = bbox[1] - 20  # Place text slightly above the bounding box

# Add text to the image
cv2.putText(image, text, (text_x, text_y), font, font_scale, font_color, font_thickness)

# Save the result image
cv2.imwrite(output_path, image)

print(f"Transformed image saved at: {output_path}")
