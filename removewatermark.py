#Removing Watermark
import cv2
import numpy as np

def add_watermark(input_image_path, output_image_path, watermark_text, position):
    # Load the original image
    image = cv2.imread(input_image_path)
    
    # Set the font and get the size of the text
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thickness = 2
    text_size = cv2.getTextSize(watermark_text, font, font_scale, font_thickness)[0]
    
    # Calculate the position
    if position == 'bottom-right':
        text_x = image.shape[1] - text_size[0] - 10
        text_y = image.shape[0] - text_size[1] - 10
    elif position == 'top-left':
        text_x = 10
        text_y = text_size[1] + 10
    else:
        raise ValueError("Position must be 'bottom-right' or 'top-left'")
    
    # Add the text to the image
    cv2.putText(image, watermark_text, (text_x, text_y), font, font_scale, (255, 255, 255), font_thickness)
    
    # Save the output image
    cv2.imwrite(output_image_path, image)

def create_watermark_mask(image_path, watermark_text, position):
    # Load the image
    image = cv2.imread(image_path)
    
    # Create a blank mask with the same dimensions as the image
    mask = np.zeros_like(image[:, :, 0])
    
    # Set the font and get the size of the text
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thickness = 2
    text_size = cv2.getTextSize(watermark_text, font, font_scale, font_thickness)[0]
    
    # Calculate the position
    if position == 'bottom-right':
        text_x = image.shape[1] - text_size[0] - 10
        text_y = image.shape[0] - text_size[1] - 10
    elif position == 'top-left':
        text_x = 10
        text_y = text_size[1] + 10
    else:
        raise ValueError("Position must be 'bottom-right' or 'top-left'")
    
    # Add the text to the mask
    cv2.putText(mask, watermark_text, (text_x, text_y), font, font_scale, (255, 255, 255), font_thickness)
    
    return mask

def remove_watermark(image_path, mask_path, output_image_path):
    # Load the original image and the mask
    image = cv2.imread(image_path)
    mask = cv2.imread(mask_path, 0)
    
    # Apply inpainting to remove the watermark
    result = cv2.inpaint(image, mask, inpaintRadius=3, flags=cv2.INPAINT_TELEA)
    
    # Save the output image
    cv2.imwrite(output_image_path, result)

# Example usage

# Paths
input_image_path = 'C:/Users/Sagar H S/Documents/mini project/watermarked.jpg'
watermarked_image_path = 'C:/Users/Sagar H S/Documents/mini project/output_with_watermark.jpg'
watermark_mask_path = 'C:/Users/Sagar H S/Documents/mini project/watermark_mask.jpg'
output_image_path = 'C:/Users/Sagar H S/Documents/mini project/output_without_watermark.jpg'

# Add a watermark
add_watermark(input_image_path, watermarked_image_path, 'sagar', 'bottom-right')

# Create a mask for the watermark
mask = create_watermark_mask(watermarked_image_path, 'sagar', 'bottom-right')
cv2.imwrite(watermark_mask_path, mask)

# Remove the watermark
remove_watermark(watermarked_image_path, watermark_mask_path, output_image_path)
