import glfw


def run():
	# http://www.glfw.org/docs/3.0/group__init.html#ga317aac130a235ab08c6db0834907d85e
	if not glfw.Init():
		raise Exception('Failed to initialize glfw!')

	windows = []

	for x in xrange(4):
		# http://www.glfw.org/docs/3.0/group__window.html#ga5c336fddf2cbb5b92f65f10fb6043344
		window = glfw.CreateWindow(800, 600, 'Window #%i' % x, None, None)
		windows.append(window)


	while len(windows):
		# http://www.glfw.org/docs/3.0/group__window.html#ga37bd57223967b4211d60ca1a0bf3c832
		glfw.PollEvents()

		for window in windows:
			# http://www.glfw.org/docs/3.0/group__input.html#gadd341da06bc8d418b4dc3a3518af9ad2
			if glfw.GetKey(window, glfw.KEY_ESCAPE):
				# http://www.glfw.org/docs/3.0/group__window.html#ga49c449dde2a6f87d996f4daaa09d6708
				glfw.SetWindowShouldClose(window, True)

			# http://www.glfw.org/docs/3.0/group__window.html#ga24e02fbfefbb81fc45320989f8140ab5
			if glfw.WindowShouldClose(window):
				# http://www.glfw.org/docs/3.0/group__window.html#gacdf43e51376051d2c091662e9fe3d7b2
				glfw.DestroyWindow(window)
				windows.remove(window)

			# http://www.glfw.org/docs/3.0/group__context.html#ga1c04dc242268f827290fe40aa1c91157
			glfw.MakeContextCurrent(window)

			## render something

			# http://www.glfw.org/docs/3.0/group__context.html#ga15a5a1ee5b3c2ca6b15ca209a12efd14
			glfw.SwapBuffers(window)


	# http://www.glfw.org/docs/3.0/group__init.html#gaaae48c0a18607ea4a4ba951d939f0901
	glfw.Terminate()


if __name__ == '__main__':
	run()
