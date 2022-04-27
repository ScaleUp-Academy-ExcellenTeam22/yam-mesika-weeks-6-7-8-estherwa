from PIL import Image

def get_the_image_decryption(path):
    """
    The function obtains a path for a file and uses the library imported   to iterate over the image pixel and check
    different things.
    :param path: path to open .
    :return: The  message.
    """


    img = Image.open(path).load()

    for width in range(img.size[0]):
        term = ""
        for height in range(img.size[1]):
            if img[width, height] ==1:
                term += chr(width)
    return term



