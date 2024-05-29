import OpenGL.GL as GL

def get_file_contents(filename):
    with open(filename, 'r') as file:
        return file.read()

class Shader:
    def __init__(self, vertex_file, fragment_file):
        vertex_code = get_file_contents(vertex_file)
        fragment_code = get_file_contents(fragment_file)

        vertex_shader = GL.glCreateShader(GL.GL_VERTEX_SHADER)
        GL.glShaderSource(vertex_shader, vertex_code)
        GL.glCompileShader(vertex_shader)
        self._check_compile_errors(vertex_shader, "VERTEX")

        fragment_shader = GL.glCreateShader(GL.GL_FRAGMENT_SHADER)
        GL.glShaderSource(fragment_shader, fragment_code)
        GL.glCompileShader(fragment_shader)
        self._check_compile_errors(fragment_shader, "FRAGMENT")

        self.ID = GL.glCreateProgram()
        GL.glAttachShader(self.ID, vertex_shader)
        GL.glAttachShader(self.ID, fragment_shader)
        GL.glLinkProgram(self.ID)
        self._check_compile_errors(self.ID, "PROGRAM")

        GL.glDeleteShader(vertex_shader)
        GL.glDeleteShader(fragment_shader)

    def activate(self):
        GL.glUseProgram(self.ID)

    def delete(self):
        GL.glDeleteProgram(self.ID)

    def _check_compile_errors(self, shader, shader_type):
        if shader_type != "PROGRAM":
            success = GL.glGetShaderiv(shader, GL.GL_COMPILE_STATUS)
            if not success:
                info_log = GL.glGetShaderInfoLog(shader)
                print(f"ERROR::SHADER_COMPILATION_ERROR of type: {shader_type}\n{info_log.decode('utf-8')}\n{'-'*80}")
        else:
            success = GL.glGetProgramiv(shader, GL.GL_LINK_STATUS)
            if not success:
                info_log = GL.glGetProgramInfoLog(shader)
                print(f"ERROR::PROGRAM_LINKING_ERROR of type: {shader_type}\n{info_log.decode('utf-8')}\n{'-'*80}")
