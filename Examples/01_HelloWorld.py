import glfw


glfw.Init()
print glfw.GetVersionString()

window = glfw.CreateWindow(800, 600, 'GLFW3 Window', None, None)
glfw.MakeContextCurrent(window)

while True:
	glfw.PollEvents()

	if glfw.GetKey(window, glfw.KEY_ESCAPE) or glfw.WindowShouldClose(window):
		break

	glfw.SwapBuffers(window)

glfw.Terminate()
