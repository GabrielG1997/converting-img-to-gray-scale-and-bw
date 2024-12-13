from PIL import Image # type: ignore

def load_image(file_path):
    """Upload an image in formats such as JPEG or PNG."""
    img = Image.open(file_path)
    img = img.convert("RGB")  # Ensures the image is in RGB format
    width, height = img.size
    pixels = list(img.getdata())  # Gets the pixels as a list of tuples (R, G, B)
    flat_pixels = [value for pixel in pixels for value in pixel]  # Flatten to a simple list
    return width, height, flat_pixels

def save_image(file_path, width, height, pixels, mode="RGB"):
    """Saves an image in formats such as JPEG or PNG."""
    img = Image.new(mode, (width, height))
    if mode == "RGB":
        data = [(pixels[i], pixels[i+1], pixels[i+2]) for i in range(0, len(pixels), 3)]
    elif mode == "L":
        data = pixels
    img.putdata(data)
    img.save(file_path)

def to_grayscale(pixels):
    """Converts a color image to grayscale."""
    grayscale_pixels = []
    for i in range(0, len(pixels), 3):
        r, g, b = pixels[i], pixels[i+1], pixels[i+2]
        gray = int(0.3 * r + 0.59 * g + 0.11 * b)  # Luminance formula
        grayscale_pixels.append(gray)
    return grayscale_pixels

def to_binary(pixels, threshold=127):
    """Converts a grayscale image to black and white."""
    binary_pixels = []
    for gray in pixels:
        binary = 255 if gray > threshold else 0
        binary_pixels.append(binary)
    return binary_pixels

# Usage example
if __name__ == "__main__":
    # Path to input and output image
    input_path = r"C:\Users\USER\Desktop\example.png"
    grayscale_path = r"C:\Users\USER\Desktop\example_gray.png"
    binary_path = r"C:\Users\USER\Desktop\example_bw.png"

    # Upload image
    width, height, pixels = load_image(input_path)

    # Convert to grayscale
    grayscale_pixels = to_grayscale(pixels)
    save_image(grayscale_path, width, height, grayscale_pixels, mode="L")

    # Convert to black and white
    binary_pixels = to_binary(grayscale_pixels)
    save_image(binary_path, width, height, binary_pixels, mode="L")

    print("Conversions complete!")
