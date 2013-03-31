import CParser

parser = CParser.CParser('glfw3.h', processAll=False)
parser.processAll(noCacheWarning=False)


type_to_ctype_map = {
	'char': 'ctypes.c_char',
	'wchar': 'ctypes.c_wchar',
	'unsigned char': 'ctypes.c_ubyte',
	'short': 'ctypes.c_short',
	'short int': 'ctypes.c_short',
	'unsigned short': 'ctypes.c_ushort',
	'unsigned short int': 'ctypes.c_ushort',
	'int': 'ctypes.c_int',
	'unsigned': 'ctypes.c_uint',
	'unsigned int': 'ctypes.c_uint',
	'long': 'ctypes.c_long',
	'long int': 'ctypes.c_long',
	'unsigned long': 'ctypes.c_ulong',
	'unsigned long int': 'ctypes.c_ulong',
	'__int64': 'ctypes.c_longlong',
	'long long': 'ctypes.c_longlong',
	'long long int': 'ctypes.c_longlong',
	'unsigned __int64': 'ctypes.c_ulonglong',
	'unsigned long long': 'ctypes.c_ulonglong',
	'unsigned long long int': 'ctypes.c_ulonglong',
	'float': 'ctypes.c_float',
	'double': 'ctypes.c_double',
	'long double': 'ctypes.c_longdouble'
}

pointer_type_to_ctype_map = {
	'char': 'ctypes.c_char_p',
	'wchar': 'ctypes.c_wchar_p',
	'void': 'ctypes.c_void_p'
}


def type_to_ctype(type_def):
	mods = type_def[1:][:]
	cls = None

	if len(type_def) > 1 and type_def[1] == '*' and type_def[0] in pointer_type_to_ctype_map:
		cls = pointer_type_to_ctype_map[type_def[0]]
		mods = type_def[2:]

	elif type_def[0] in type_to_ctype_map:
		cls = type_to_ctype_map[type_def[0]]

	elif type_def[0] in parser.defs['types']:
		cls = type_def[0]

	elif type_def[0] == 'void':
		cls = 'None'

	while mods:
		modifier = mods.pop(0)

		if isinstance(modifier, basestring):
			if modifier[0] in '*&':
				for _ in modifier:
					cls = 'ctypes.POINTER(%s)' % cls

		elif isinstance(modifier, list):
			for array_size in modifier:
				if array_size == -1:
					cls = 'ctypes.POINTER(%s)' % cls
				else:
					cls = '%s * %i' % (cls, array_size)

	return cls

with open('libglfw.py', 'w') as wrapper:
	wrapper.write('import ctypes\n\n\n')
	wrapper.write('''\
glfwLib_paths = ['glfw3.dll', 'libglfw3.so', 'glfw.dll', 'libglfw.so']
glfwLib = None

for library_path in glfwLib_paths:
	try:
		glfwLib = ctypes.cdll.LoadLibrary(library_path)
		break
	except OSError:
		pass

if not glfwLib:
	raise Exception('Unable to find GLFW3 library: {}'.format(', '.join(glfwLib_paths)))


''')

	wrapper.write('## MACROS\n')
	for macro_name, macro_value in parser.defs['macros'].iteritems():
		if macro_value:
			wrapper.write('%s = %s\n' % (macro_name, macro_value))
	wrapper.write('\n\n')

	wrapper.write('## TYPES\n')
	for struct_name, struct_value in parser.defs['types'].iteritems():
		if struct_name.startswith('struct '):
			continue

		if struct_value[0].startswith('struct'):
			wrapper.write('class %s(ctypes.Structure):\n' % struct_name)
			_, struct_name = struct_value[0].split(' ')

			if struct_name in parser.defs['structs']:
				struct = parser.defs['structs'][struct_name]
				if len(struct['members']):
					wrapper.write('\t_fields_ = (\n')
					for member_name, member_value, _ in struct['members']:
						wrapper.write('\t\t(\'%s\', %s),\n' % (member_name, type_to_ctype(member_value)))
					wrapper.write('\t)\n\n')

				else:
					wrapper.write('\t_fields_ = ()\n\n')

		else:
			result_type, argument_types, _ = struct_value
			restype = type_to_ctype([result_type])

			argtypes = []
			for wtf, argument_type, wtf in argument_types:
				argtypes.append(type_to_ctype(argument_type))
			if argtypes == ['None']:
				argtypes = ''

			wrapper.write('%s = ctypes.CFUNCTYPE(%s, %s)\n\n' % (struct_name, restype, ', '.join(argtypes)))
	wrapper.write('\n')

	wrapper.write('## FUNCTIONS\n')
	for function_name, (result_type, argument_types) in parser.defs['functions'].iteritems():
		wrapper.write('%s = glfwLib.%s\n' % (function_name, function_name))

		processed_arg_types = []
		python_arg_names = []
		for argument_name, argument_type_def, _ in argument_types:
			processed_arg_types.append(type_to_ctype(argument_type_def))
			python_arg_names.append(argument_name)

		arg_types = ', '.join(processed_arg_types)
		if processed_arg_types == ['None']:
			arg_types = ''
		elif len(processed_arg_types) == 1:
			arg_types += ', '

		if python_arg_names == [None]:
			python_arg_names = ''

		wrapper.write('%s.argtypes = (%s)\n' % (function_name, arg_types))
		wrapper.write('%s.restype = %s\n' % (function_name, type_to_ctype(result_type)))
		#wrapper.write('def %s(%s):\n\treturn _%s(%s)\n' % (function_name, ', '.join(python_arg_names), function_name, ', '.join(python_arg_names)))
		wrapper.write('\n')
