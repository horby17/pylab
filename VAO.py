from OpenGL.GL import *

class VAO:
    def __init__(self):
        self.ID = glGenVertexArrays(1)

    def link_attrib(self, vbo, layout, num_components, type, stride, offset):
        vbo.bind()
        glVertexAttribPointer(layout, num_components, type, GL_FALSE, stride, ctypes.c_void_p(offset))
        glEnableVertexAttribArray(layout)
        vbo.unbind()

    def bind(self):
        glBindVertexArray(self.ID)

    def unbind(self):
        glBindVertexArray(0)

    def delete(self):
        glDeleteVertexArrays(1, [self.ID])
