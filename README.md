# glfw3

## Description
A Python 2.x wrapper for [GLFW 3](https://github.com/elmindreda/glfw) using ctypes. PyPy compatible.

## Example
```python
from glfw import *

glfwInit()

window = glfwCreateWindow(800, 600, 'GLFW3')
glfwMakeContextCurrent(window)

while not glfwWindowShouldClose(window):
    glfwPollEvents()
    glfwSwapBuffers(window)

glfwTerminate()
```

## Included
libglfw.py
	An automatically generated wrapper for glfw3.h

glfw.py
	An abstraction layer above libglfw.py, so you don't need to muck about with ctypes.
