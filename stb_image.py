from PIL import Image
import numpy as np

def load_texture(path):
    image = Image.open(path)
    image = image.transpose(Image.FLIP_TOP_BOTTOM)
    img_data = np.array(image, dtype=np.uint8)
    return img_data, image.width, image.height
