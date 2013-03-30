# glfw3

## Description
A Python 2.x wrapper for [GLFW 3](https://github.com/elmindreda/glfw) using ctypes. PyPy compatible.

## Example
```python
import glfw

glfw.Init()
window = glfw.CreateWindow(800, 600, 'GLFW3', None, None)
while not glfw.WindowShouldClose(window):
    glfw.PollEvents()
    glfw.SwapBuffers(window)
glfw.Terminate()
```
