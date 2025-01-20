# image_to_ascii/image_to_ascii.py

from PIL import Image

# ASCII characters used to build the output text
ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    return image.resize((new_width, new_height))

def grayscale_image(image):
    return image.convert("L")

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = "".join([ASCII_CHARS[pixel // 32] for pixel in pixels])
    return ascii_str

def convert_image_to_ascii(image_path, new_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Unable to open image file {image_path}. {e}")
        return

    image = resize_image(image, new_width)
    image = grayscale_image(image)
    
    ascii_str = pixels_to_ascii(image)
    img_width = image.width
    ascii_str_len = len(ascii_str)
    ascii_img = "\n".join([ascii_str[i:i + img_width] for i in range(0, ascii_str_len, img_width)])

print(ascii_img)
    return ascii_img

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        convert_image_to_ascii(sys.argv[1])
    else:
        print("Usage: python image-ascii.py <image_path>")
