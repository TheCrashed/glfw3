import ctypes


glfwDLL = ctypes.cdll.LoadLibrary('glfw3.dll')


## MACROS
VERSION_MAJOR = 3
VERSION_MINOR = 0
VERSION_REVISION = 0
RELEASE = 0
PRESS = 1
KEY_SPACE = 32
KEY_APOSTROPHE = 39
KEY_COMMA = 44
KEY_MINUS = 45
KEY_PERIOD = 46
KEY_SLASH = 47
KEY_0 = 48
KEY_1 = 49
KEY_2 = 50
KEY_3 = 51
KEY_4 = 52
KEY_5 = 53
KEY_6 = 54
KEY_7 = 55
KEY_8 = 56
KEY_9 = 57
KEY_SEMICOLON = 59
KEY_EQUAL = 61
KEY_A = 65
KEY_B = 66
KEY_C = 67
KEY_D = 68
KEY_E = 69
KEY_F = 70
KEY_G = 71
KEY_H = 72
KEY_I = 73
KEY_J = 74
KEY_K = 75
KEY_L = 76
KEY_M = 77
KEY_N = 78
KEY_O = 79
KEY_P = 80
KEY_Q = 81
KEY_R = 82
KEY_S = 83
KEY_T = 84
KEY_U = 85
KEY_V = 86
KEY_W = 87
KEY_X = 88
KEY_Y = 89
KEY_Z = 90
KEY_LEFT_BRACKET = 91
KEY_BACKSLASH = 92
KEY_RIGHT_BRACKET = 93
KEY_GRAVE_ACCENT = 96
KEY_WORLD_1 = 161
KEY_WORLD_2 = 162
KEY_ESCAPE = 256
KEY_ENTER = 257
KEY_TAB = 258
KEY_BACKSPACE = 259
KEY_INSERT = 260
KEY_DELETE = 261
KEY_RIGHT = 262
KEY_LEFT = 263
KEY_DOWN = 264
KEY_UP = 265
KEY_PAGE_UP = 266
KEY_PAGE_DOWN = 267
KEY_HOME = 268
KEY_END = 269
KEY_CAPS_LOCK = 280
KEY_SCROLL_LOCK = 281
KEY_NUM_LOCK = 282
KEY_PRINT_SCREEN = 283
KEY_PAUSE = 284
KEY_F1 = 290
KEY_F2 = 291
KEY_F3 = 292
KEY_F4 = 293
KEY_F5 = 294
KEY_F6 = 295
KEY_F7 = 296
KEY_F8 = 297
KEY_F9 = 298
KEY_F10 = 299
KEY_F11 = 300
KEY_F12 = 301
KEY_F13 = 302
KEY_F14 = 303
KEY_F15 = 304
KEY_F16 = 305
KEY_F17 = 306
KEY_F18 = 307
KEY_F19 = 308
KEY_F20 = 309
KEY_F21 = 310
KEY_F22 = 311
KEY_F23 = 312
KEY_F24 = 313
KEY_F25 = 314
KEY_KP_0 = 320
KEY_KP_1 = 321
KEY_KP_2 = 322
KEY_KP_3 = 323
KEY_KP_4 = 324
KEY_KP_5 = 325
KEY_KP_6 = 326
KEY_KP_7 = 327
KEY_KP_8 = 328
KEY_KP_9 = 329
KEY_KP_DECIMAL = 330
KEY_KP_DIVIDE = 331
KEY_KP_MULTIPLY = 332
KEY_KP_SUBTRACT = 333
KEY_KP_ADD = 334
KEY_KP_ENTER = 335
KEY_KP_EQUAL = 336
KEY_LEFT_SHIFT = 340
KEY_LEFT_CONTROL = 341
KEY_LEFT_ALT = 342
KEY_LEFT_SUPER = 343
KEY_RIGHT_SHIFT = 344
KEY_RIGHT_CONTROL = 345
KEY_RIGHT_ALT = 346
KEY_RIGHT_SUPER = 347
KEY_MENU = 348
KEY_LAST = 348
KEY_ESC = 256
KEY_DEL = 261
KEY_PAGEUP = 266
KEY_PAGEDOWN = 267
KEY_KP_NUM_LOCK = 282
KEY_LCTRL = 341
KEY_LSHIFT = 340
KEY_LALT = 342
KEY_LSUPER = 343
KEY_RCTRL = 345
KEY_RSHIFT = 344
KEY_RALT = 346
KEY_RSUPER = 347
MOUSE_BUTTON_1 = 0
MOUSE_BUTTON_2 = 1
MOUSE_BUTTON_3 = 2
MOUSE_BUTTON_4 = 3
MOUSE_BUTTON_5 = 4
MOUSE_BUTTON_6 = 5
MOUSE_BUTTON_7 = 6
MOUSE_BUTTON_8 = 7
MOUSE_BUTTON_LAST = 7
MOUSE_BUTTON_LEFT = 0
MOUSE_BUTTON_RIGHT = 1
MOUSE_BUTTON_MIDDLE = 2
JOYSTICK_1 = 0
JOYSTICK_2 = 1
JOYSTICK_3 = 2
JOYSTICK_4 = 3
JOYSTICK_5 = 4
JOYSTICK_6 = 5
JOYSTICK_7 = 6
JOYSTICK_8 = 7
JOYSTICK_9 = 8
JOYSTICK_10 = 9
JOYSTICK_11 = 10
JOYSTICK_12 = 11
JOYSTICK_13 = 12
JOYSTICK_14 = 13
JOYSTICK_15 = 14
JOYSTICK_16 = 15
JOYSTICK_LAST = 15
NO_ERROR = 0
NOT_INITIALIZED = 0x00070001
NO_CURRENT_CONTEXT = 0x00070002
INVALID_ENUM = 0x00070003
INVALID_VALUE = 0x00070004
OUT_OF_MEMORY = 0x00070005
API_UNAVAILABLE = 0x00070006
VERSION_UNAVAILABLE = 0x00070007
PLATFORM_ERROR = 0x00070008
FORMAT_UNAVAILABLE = 0x00070009
FOCUSED = 0x00020001
ICONIFIED = 0x00020002
SHOULD_CLOSE = 0x00020003
RESIZABLE = 0x00022007
VISIBLE = 0x00022008
POSITION_X = 0x00022009
POSITION_Y = 0x0002200A
CONTEXT_REVISION = 0x00020004
RED_BITS = 0x00021000
GREEN_BITS = 0x00021001
BLUE_BITS = 0x00021002
ALPHA_BITS = 0x00021003
DEPTH_BITS = 0x00021004
STENCIL_BITS = 0x00021005
ACCUM_RED_BITS = 0x00021006
ACCUM_GREEN_BITS = 0x00021007
ACCUM_BLUE_BITS = 0x00021008
ACCUM_ALPHA_BITS = 0x00021009
AUX_BUFFERS = 0x0002100A
STEREO = 0x0002100B
SAMPLES = 0x0002100C
SRGB_CAPABLE = 0x0002100D
CLIENT_API = 0x00022000
CONTEXT_VERSION_MAJOR = 0x00022001
CONTEXT_VERSION_MINOR = 0x00022002
CONTEXT_ROBUSTNESS = 0x00022003
OPENGL_FORWARD_COMPAT = 0x00022004
OPENGL_DEBUG_CONTEXT = 0x00022005
OPENGL_PROFILE = 0x00022006
OPENGL_API = 0x00000001
OPENGL_ES_API = 0x00000002
NO_ROBUSTNESS = 0x00000000
NO_RESET_NOTIFICATION = 0x00000001
LOSE_CONTEXT_ON_RESET = 0x00000002
OPENGL_NO_PROFILE = 0x00000000
OPENGL_CORE_PROFILE = 0x00000001
OPENGL_COMPAT_PROFILE = 0x00000002
CURSOR_MODE = 0x00030001
STICKY_KEYS = 0x00030002
STICKY_MOUSE_BUTTONS = 0x00030003
CURSOR_NORMAL = 0x00040001
CURSOR_HIDDEN = 0x00040002
CURSOR_CAPTURED = 0x00040003
PRESENT = 0x00050001
AXES = 0x00050002
BUTTONS = 0x00050003
GAMMA_RAMP_SIZE = 256
MONITOR_WIDTH_MM = 0x00060001
MONITOR_HEIGHT_MM = 0x00060002
MONITOR_POS_X = 0x00060003
MONITOR_POS_Y = 0x00060004
CONNECTED = 0x00061000
DISCONNECTED = 0x00061001


## TYPES
glproc = ctypes.CFUNCTYPE(None, )

class monitor(ctypes.Structure):
		_fields_ = []

class window(ctypes.Structure):
		_fields_ = []

errorfun = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_char_p)

windowposfun = ctypes.CFUNCTYPE(None, ctypes.POINTER(window), ctypes.c_int, ctypes.c_int)

windowsizefun = ctypes.CFUNCTYPE(None, ctypes.POINTER(window), ctypes.c_int, ctypes.c_int)

windowclosefun = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(window))

windowrefreshfun = ctypes.CFUNCTYPE(None, ctypes.POINTER(window))

windowfocusfun = ctypes.CFUNCTYPE(None, ctypes.POINTER(window), ctypes.c_int)

windowiconifyfun = ctypes.CFUNCTYPE(None, ctypes.POINTER(window), ctypes.c_int)

mousebuttonfun = ctypes.CFUNCTYPE(None, ctypes.POINTER(window), ctypes.c_int, ctypes.c_int)

cursorposfun = ctypes.CFUNCTYPE(None, ctypes.POINTER(window), ctypes.c_int, ctypes.c_int)

cursorenterfun = ctypes.CFUNCTYPE(None, ctypes.POINTER(window), ctypes.c_int)

scrollfun = ctypes.CFUNCTYPE(None, ctypes.POINTER(window), ctypes.c_double, ctypes.c_double)

keyfun = ctypes.CFUNCTYPE(None, ctypes.POINTER(window), ctypes.c_int, ctypes.c_int)

charfun = ctypes.CFUNCTYPE(None, ctypes.POINTER(window), ctypes.c_int)

monitorfun = ctypes.CFUNCTYPE(None, ctypes.POINTER(monitor), ctypes.c_int)

class vidmode(ctypes.Structure):
	_fields_ = [
		('width', ctypes.c_int),
		('height', ctypes.c_int),
		('redBits', ctypes.c_int),
		('blueBits', ctypes.c_int),
		('greenBits', ctypes.c_int),
	]

class gammaramp(ctypes.Structure):
	_fields_ = [
		('red', ctypes.c_ushort * 256),
		('green', ctypes.c_ushort * 256),
		('blue', ctypes.c_ushort * 256),
	]


## FUNCTIONS
Init = glfwDLL.glfwInit
Init.argtypes = []
Init.restype = ctypes.c_int

Terminate = glfwDLL.glfwTerminate
Terminate.argtypes = []
Terminate.restype = None

GetVersion = glfwDLL.glfwGetVersion
GetVersion.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
GetVersion.restype = None

GetVersionString = glfwDLL.glfwGetVersionString
GetVersionString.argtypes = []
GetVersionString.restype = ctypes.c_char_p

SetErrorCallback = glfwDLL.glfwSetErrorCallback
SetErrorCallback.argtypes = [errorfun]
SetErrorCallback.restype = None

GetMonitors = glfwDLL.glfwGetMonitors
GetMonitors.argtypes = [ctypes.POINTER(ctypes.c_int)]
GetMonitors.restype = ctypes.POINTER(ctypes.POINTER(monitor))

GetPrimaryMonitor = glfwDLL.glfwGetPrimaryMonitor
GetPrimaryMonitor.argtypes = []
GetPrimaryMonitor.restype = ctypes.POINTER(monitor)

GetMonitorParam = glfwDLL.glfwGetMonitorParam
GetMonitorParam.argtypes = [ctypes.POINTER(monitor), ctypes.c_int]
GetMonitorParam.restype = ctypes.c_int

GetMonitorName = glfwDLL.glfwGetMonitorName
GetMonitorName.argtypes = [ctypes.POINTER(monitor)]
GetMonitorName.restype = ctypes.c_char_p

SetMonitorCallback = glfwDLL.glfwSetMonitorCallback
SetMonitorCallback.argtypes = [monitorfun]
SetMonitorCallback.restype = None

GetVideoModes = glfwDLL.glfwGetVideoModes
GetVideoModes.argtypes = [ctypes.POINTER(monitor), ctypes.POINTER(ctypes.c_int)]
GetVideoModes.restype = ctypes.POINTER(vidmode)

GetVideoMode = glfwDLL.glfwGetVideoMode
GetVideoMode.argtypes = [ctypes.POINTER(monitor)]
GetVideoMode.restype = vidmode

SetGamma = glfwDLL.glfwSetGamma
SetGamma.argtypes = [ctypes.c_float]
SetGamma.restype = None

GetGammaRamp = glfwDLL.glfwGetGammaRamp
GetGammaRamp.argtypes = [ctypes.POINTER(gammaramp)]
GetGammaRamp.restype = None

SetGammaRamp = glfwDLL.glfwSetGammaRamp
SetGammaRamp.argtypes = [ctypes.POINTER(gammaramp)]
SetGammaRamp.restype = None

DefaultWindowHints = glfwDLL.glfwDefaultWindowHints
DefaultWindowHints.argtypes = []
DefaultWindowHints.restype = None

WindowHint = glfwDLL.glfwWindowHint
WindowHint.argtypes = [ctypes.c_int, ctypes.c_int]
WindowHint.restype = None

CreateWindow = glfwDLL.glfwCreateWindow
CreateWindow.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(monitor), ctypes.POINTER(window)]
CreateWindow.restype = ctypes.POINTER(window)

DestroyWindow = glfwDLL.glfwDestroyWindow
DestroyWindow.argtypes = [ctypes.POINTER(window)]
DestroyWindow.restype = None

SetWindowTitle = glfwDLL.glfwSetWindowTitle
SetWindowTitle.argtypes = [ctypes.POINTER(window), ctypes.c_char_p]
SetWindowTitle.restype = None

GetWindowSize = glfwDLL.glfwGetWindowSize
GetWindowSize.argtypes = [ctypes.POINTER(window), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
GetWindowSize.restype = None

SetWindowSize = glfwDLL.glfwSetWindowSize
SetWindowSize.argtypes = [ctypes.POINTER(window), ctypes.c_int, ctypes.c_int]
SetWindowSize.restype = None

IconifyWindow = glfwDLL.glfwIconifyWindow
IconifyWindow.argtypes = [ctypes.POINTER(window)]
IconifyWindow.restype = None

RestoreWindow = glfwDLL.glfwRestoreWindow
RestoreWindow.argtypes = [ctypes.POINTER(window)]
RestoreWindow.restype = None

ShowWindow = glfwDLL.glfwShowWindow
ShowWindow.argtypes = [ctypes.POINTER(window)]
ShowWindow.restype = None

HideWindow = glfwDLL.glfwHideWindow
HideWindow.argtypes = [ctypes.POINTER(window)]
HideWindow.restype = None

GetWindowMonitor = glfwDLL.glfwGetWindowMonitor
GetWindowMonitor.argtypes = [ctypes.POINTER(window)]
GetWindowMonitor.restype = ctypes.POINTER(monitor)

GetWindowParam = glfwDLL.glfwGetWindowParam
GetWindowParam.argtypes = [ctypes.POINTER(window), ctypes.c_int]
GetWindowParam.restype = ctypes.c_int

SetWindowUserPointer = glfwDLL.glfwSetWindowUserPointer
SetWindowUserPointer.argtypes = [ctypes.POINTER(window), ctypes.c_void_p]
SetWindowUserPointer.restype = None

GetWindowUserPointer = glfwDLL.glfwGetWindowUserPointer
GetWindowUserPointer.argtypes = [ctypes.POINTER(window)]
GetWindowUserPointer.restype = ctypes.c_void_p

SetWindowPosCallback = glfwDLL.glfwSetWindowPosCallback
SetWindowPosCallback.argtypes = [ctypes.POINTER(window), windowposfun]
SetWindowPosCallback.restype = None

SetWindowSizeCallback = glfwDLL.glfwSetWindowSizeCallback
SetWindowSizeCallback.argtypes = [ctypes.POINTER(window), windowsizefun]
SetWindowSizeCallback.restype = None

SetWindowCloseCallback = glfwDLL.glfwSetWindowCloseCallback
SetWindowCloseCallback.argtypes = [ctypes.POINTER(window), windowclosefun]
SetWindowCloseCallback.restype = None

SetWindowRefreshCallback = glfwDLL.glfwSetWindowRefreshCallback
SetWindowRefreshCallback.argtypes = [ctypes.POINTER(window), windowrefreshfun]
SetWindowRefreshCallback.restype = None

SetWindowFocusCallback = glfwDLL.glfwSetWindowFocusCallback
SetWindowFocusCallback.argtypes = [ctypes.POINTER(window), windowfocusfun]
SetWindowFocusCallback.restype = None

SetWindowIconifyCallback = glfwDLL.glfwSetWindowIconifyCallback
SetWindowIconifyCallback.argtypes = [ctypes.POINTER(window), windowiconifyfun]
SetWindowIconifyCallback.restype = None

PollEvents = glfwDLL.glfwPollEvents
PollEvents.argtypes = []
PollEvents.restype = None

WaitEvents = glfwDLL.glfwWaitEvents
WaitEvents.argtypes = []
WaitEvents.restype = None

GetInputMode = glfwDLL.glfwGetInputMode
GetInputMode.argtypes = [ctypes.POINTER(window), ctypes.c_int]
GetInputMode.restype = ctypes.c_int

SetInputMode = glfwDLL.glfwSetInputMode
SetInputMode.argtypes = [ctypes.POINTER(window), ctypes.c_int, ctypes.c_int]
SetInputMode.restype = None

GetKey = glfwDLL.glfwGetKey
GetKey.argtypes = [ctypes.POINTER(window), ctypes.c_int]
GetKey.restype = ctypes.c_int

GetMouseButton = glfwDLL.glfwGetMouseButton
GetMouseButton.argtypes = [ctypes.POINTER(window), ctypes.c_int]
GetMouseButton.restype = ctypes.c_int

GetCursorPos = glfwDLL.glfwGetCursorPos
GetCursorPos.argtypes = [ctypes.POINTER(window), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
GetCursorPos.restype = None

SetCursorPos = glfwDLL.glfwSetCursorPos
SetCursorPos.argtypes = [ctypes.POINTER(window), ctypes.c_int, ctypes.c_int]
SetCursorPos.restype = None

GetScrollOffset = glfwDLL.glfwGetScrollOffset
GetScrollOffset.argtypes = [ctypes.POINTER(window), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
GetScrollOffset.restype = None

SetKeyCallback = glfwDLL.glfwSetKeyCallback
SetKeyCallback.argtypes = [ctypes.POINTER(window), keyfun]
SetKeyCallback.restype = None

SetCharCallback = glfwDLL.glfwSetCharCallback
SetCharCallback.argtypes = [ctypes.POINTER(window), charfun]
SetCharCallback.restype = None

SetMouseButtonCallback = glfwDLL.glfwSetMouseButtonCallback
SetMouseButtonCallback.argtypes = [ctypes.POINTER(window), mousebuttonfun]
SetMouseButtonCallback.restype = None

SetCursorPosCallback = glfwDLL.glfwSetCursorPosCallback
SetCursorPosCallback.argtypes = [ctypes.POINTER(window), cursorposfun]
SetCursorPosCallback.restype = None

SetCursorEnterCallback = glfwDLL.glfwSetCursorEnterCallback
SetCursorEnterCallback.argtypes = [ctypes.POINTER(window), cursorenterfun]
SetCursorEnterCallback.restype = None

SetScrollCallback = glfwDLL.glfwSetScrollCallback
SetScrollCallback.argtypes = [ctypes.POINTER(window), scrollfun]
SetScrollCallback.restype = None

GetJoystickParam = glfwDLL.glfwGetJoystickParam
GetJoystickParam.argtypes = [ctypes.c_int, ctypes.c_int]
GetJoystickParam.restype = ctypes.c_int

GetJoystickAxes = glfwDLL.glfwGetJoystickAxes
GetJoystickAxes.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_float), ctypes.c_int]
GetJoystickAxes.restype = ctypes.c_int

GetJoystickButtons = glfwDLL.glfwGetJoystickButtons
GetJoystickButtons.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_ubyte), ctypes.c_int]
GetJoystickButtons.restype = ctypes.c_int

GetJoystickName = glfwDLL.glfwGetJoystickName
GetJoystickName.argtypes = [ctypes.c_int]
GetJoystickName.restype = ctypes.c_char_p

SetClipboardString = glfwDLL.glfwSetClipboardString
SetClipboardString.argtypes = [ctypes.POINTER(window), ctypes.c_char_p]
SetClipboardString.restype = None

GetClipboardString = glfwDLL.glfwGetClipboardString
GetClipboardString.argtypes = [ctypes.POINTER(window)]
GetClipboardString.restype = ctypes.c_char_p

GetTime = glfwDLL.glfwGetTime
GetTime.argtypes = []
GetTime.restype = ctypes.c_double

SetTime = glfwDLL.glfwSetTime
SetTime.argtypes = [ctypes.c_double]
SetTime.restype = None

MakeContextCurrent = glfwDLL.glfwMakeContextCurrent
MakeContextCurrent.argtypes = [ctypes.POINTER(window)]
MakeContextCurrent.restype = None

GetCurrentContext = glfwDLL.glfwGetCurrentContext
GetCurrentContext.argtypes = []
GetCurrentContext.restype = ctypes.POINTER(window)

SwapBuffers = glfwDLL.glfwSwapBuffers
SwapBuffers.argtypes = [ctypes.POINTER(window)]
SwapBuffers.restype = None

SwapInterval = glfwDLL.glfwSwapInterval
SwapInterval.argtypes = [ctypes.c_int]
SwapInterval.restype = None

ExtensionSupported = glfwDLL.glfwExtensionSupported
ExtensionSupported.argtypes = [ctypes.c_char_p]
ExtensionSupported.restype = ctypes.c_int

GetProcAddress = glfwDLL.glfwGetProcAddress
GetProcAddress.argtypes = [ctypes.c_char_p]
GetProcAddress.restype = glproc

