from OpenGL.GL import *
import numpy as np
from PIL import Image

class Texture:
    def __init__(self, filename):
        self.ID = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.ID)

        # Set the texture wrapping parameters
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)

        # Set texture filtering parameters
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        # Load image
        image = Image.open(filename)
        image = image.transpose(Image.FLIP_TOP_BOTTOM)
        img_data = np.array(image, dtype=np.uint8)

        # Generate the texture
        if image.mode == 'RGB':
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, image.width, image.height, 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
        elif image.mode == 'RGBA':
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.width, image.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
        else:
            raise Exception("Formato de imagen no soportado")

        glGenerateMipmap(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, 0)

    def bind(self):
        glBindTexture(GL_TEXTURE_2D, self.ID)

    def unbind(self):
        glBindTexture(GL_TEXTURE_2D, 0)

    def delete(self):
        glDeleteTextures(1, [self.ID])
