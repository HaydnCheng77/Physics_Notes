from PIL import Image

def stretch_image(image_path, new_width, new_height, output_path):
    """
    Opens an image, resizes it to new dimensions (distorting it if necessary),
    and saves the result.

    Parameters:
        image_path (str): Path to the input image.
        new_width (int): New width of the image.
        new_height (int): New height of the image.
        output_path (str): Path to save the resized image.
    """
    # Open the input image
    img = Image.open(image_path)
    
    # Resize the image to the specified new dimensions using LANCZOS filter
    img_resized = img.resize((new_width, new_height), Image.LANCZOS)
    
    # Save the new image
    img_resized.save(output_path)
    print(f"Image saved as {output_path}")

if __name__ == "__main__":
    # Input image path (using a raw string for Windows file paths)
    input_image = r"C:\Users\User\Downloads\Physics Notes\GP04 Lab Report\setup.png"
    
    # Output image path
    output_image = r"C:\Users\User\Downloads\Physics Notes\GP04 Lab Report\setup_fatter.png"
    
    # Desired new dimensions (change these values to make the image "fatter")
    desired_width = 600  # Increase the width
    desired_height = 800  # Keep or adjust the height as needed
    
    stretch_image(input_image, desired_width, desired_height, output_image)
