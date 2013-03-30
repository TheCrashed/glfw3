import glfw

glfw.Init()
window = glfw.CreateWindow(800, 600, 'GLFW3', None, None)
while not glfw.WindowShouldClose(window):
    glfw.PollEvents()
    glfw.SwapBuffers(window)
glfw.Terminate()