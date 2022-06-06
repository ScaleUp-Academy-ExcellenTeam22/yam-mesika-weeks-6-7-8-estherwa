from PIL import Image
import PIL.ImageGrab


def get_the_image_decryption(path):
    """
    The function obtains a path for a file and uses the library imported   to iterate over the image pixel and check
    different things.
    :param path: path to open.
    :return: The  message.
    """
    img = PIL.Image.open(path, 'r')
    pixel = img.load()

    b_pixels = [col for row in range(img.size[0]) for col in range(img.size[1]) if pixel[row, col] == 1]

    return ''.join(chr(pixel[1]) for pixel in b_pixels)
