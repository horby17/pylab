import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from PIL import Image
import numpy as np

def load_texture(texture_path):
    img = Image.open(texture_path)
    img_data = np.array(list(img.getdata()), np.uint8)

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.width, img.height, 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    return texture_id

def create_triangle():
    glBegin(GL_TRIANGLES)
    glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0, 0.0)
    glTexCoord2f(1.0, 0.0); glVertex3f( 1.0, -1.0, 0.0)
    glTexCoord2f(0.5, 1.0); glVertex3f( 0.0,  1.0, 0.0)
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    texture_id = load_texture('../textures/fruit.jpg') # Cambia el nombre del archivo por tu imagen

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        create_triangle()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
