import numpy as np
import skimage
from skimage import io, transform

def scale_image(image=np.zeros((100,100)), new_width=100, ascii_block_size=(2,3)):

    #Resizes image so that the final  ascii version will have the same aspect ratio.

    original_width, original_height = image.shape
    aspect_ratio = original_height / float(original_width)
    w,h = ascii_block_size
    new_height = int(h/w * aspect_ratio * new_width)

    return skimage.transform.resize(image, (new_width, new_height))


def image2ascii(image=np.zeros((100,100)), new_width=100):

    def float2char(x=.1):
        # ASCII_CHARS = [ 'W','X','@','0','#', '+', ';', ':', '"','.',' ']
        # ASCII_CHARS = [ 'W','X','N','V', '=', '/', '>', '"','.',' ']
        ASCII_CHARS = [ '#', '?', '%', '.', 'S', '+', '.', '*', ':', ',', '@']
        num_chars = len(ASCII_CHARS)
        return ASCII_CHARS[ int(num_chars*x) ]

   #this is going to get called on an ndarray of float so vectorize
    float2char = np.vectorize(float2char)

    image = scale_image(image, new_width=new_width)

    #rescale so that we don't go past the end of ASCII_CHARS
    #float2char yields an ndarray of str
    #we have to flatten to a single str
    rows = ["".join(row) for row in float2char(.999*image) ]
    return "\n".join(rows)

def handle_image_conversion(image_filepath, new_width=100):

    image = np.zeros((200,200))

    try:
        image = skimage.io.imread(image_filepath, as_gray=True)
    except Exception as e:
        format_str = "Unable to open image file {image_filepath}."
        print( format_str.format(image_filepath=image_filepath))
        print(e)
        return

    image_ascii = image2ascii(image, new_width=new_width)
    print(image_ascii)

handle_image_conversion(r'.\babyyoda.jpg', new_width=50)
