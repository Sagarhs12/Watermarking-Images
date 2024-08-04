#Adding Watermark
import cv2

def add_watermark(input_image_path, output_image_path, watermark_text, position):
    # Load the original image
    image = cv2.imread('C:/Users/Sagar H S/Documents/mini project/watermarked.jpg')
    
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
    cv2.imwrite('C:/Users/Sagar H S/Documents/mini project/output1.jpg', image)

# Example usage
add_watermark('input.jpg', 'output_with_watermark.jpg', 'sagar', 'bottom-right')
