import glfw
import OpenGL.GL
import pyglet.gl


class Application(object):
	def init(self, window_width=800, window_height=600):
		if not glfw.Init():
			raise Exception('Failed to initialize glfw!')

		vidmode = glfw.GetVideoMode(glfw.GetPrimaryMonitor())
		screen_width = vidmode.width
		screen_height = vidmode.height

		window_x = (screen_width - window_width) / 2
		window_y = (screen_height - window_height) / 2

		glfw.WindowHint(glfw.CONTEXT_VERSION_MAJOR, 3)
		glfw.WindowHint(glfw.CONTEXT_VERSION_MINOR, 2)

		glfw.WindowHint(glfw.OPENGL_FORWARD_COMPAT, True)
		glfw.WindowHint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

		self.window = glfw.CreateWindow(window_width, window_height, 'GLFW PyOpenGL or pyglet.gl', None, None)
		if not self.window:
			raise Exception('Failed to create a window with opengl core profile, context version 3.2')

		glfw.SetWindowPos(self.window, window_x, window_y)

		# do not let this get garbage collected!
		self.__keyhandler = glfw.keyfun(self.on_key_press)
		glfw.SetKeyCallback(self.window, self.__keyhandler)

	def on_key_press(self, window, key, action):
		if action == glfw.RELEASE:
			if key == glfw.KEY_ESCAPE:
				self.quit = True

	def create_scene(self):
		glfw.MakeContextCurrent(self.window)
		OpenGL.GL.glClearColor(0.2, 0.75, 0.85, 1.0)

	def draw(self):
		pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)

	def run(self):
		self.quit = False
		while not self.quit:
			glfw.PollEvents()

			if glfw.WindowShouldClose(self.window):
				self.quit = True

			self.draw()

			glfw.SwapBuffers(self.window)


if __name__ == '__main__':
	game = Application()
	game.init()
	game.create_scene()
	game.run()
