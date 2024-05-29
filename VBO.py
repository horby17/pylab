from OpenGL.GL import *

class VBO:
    def __init__(self, data):
        self.ID = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.ID)
        glBufferData(GL_ARRAY_BUFFER, data.nbytes, data, GL_STATIC_DRAW)

    def bind(self):
        glBindBuffer(GL_ARRAY_BUFFER, self.ID)

    def unbind(self):
        glBindBuffer(GL_ARRAY_BUFFER, 0)

    def delete(self):
        glDeleteBuffers(1, [self.ID])
