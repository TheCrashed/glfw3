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

		elif isinstance(modifier, tuple):
			raise Exception('FUCK')
			is_pointer = False
			convention = '__cdecl'

			if len(mods) == 0:
				raise Exception('wtf?')

	return cls

with open('glfw.py', 'w') as wrapper:
	wrapper.write('import ctypes\n\n\n')
	wrapper.write('glfwDLL = ctypes.cdll.LoadLibrary(\'glfw3.dll\')\n\n\n')

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
					wrapper.write('\t_fields_ = [\n')
					for member_name, member_value, _ in struct['members']:
						wrapper.write('\t\t(\'%s\', %s),\n' % (member_name, type_to_ctype(member_value)))
					wrapper.write('\t]\n\n')

				else:
					wrapper.write('\t\t_fields_ = []\n\n')

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
		wrapper.write('%s = glfwDLL.%s\n' % (function_name, function_name))

		processed_arg_types = []
		for argument_name, argument_type_def, _ in argument_types:
			processed_arg_types.append(type_to_ctype(argument_type_def))

		arg_types = ', '.join(processed_arg_types)
		if processed_arg_types == ['None']:
			arg_types = ''

		wrapper.write('%s.argtypes = [%s]\n' % (function_name, arg_types))
		wrapper.write('%s.restype = %s\n' % (function_name, type_to_ctype(result_type)))
		wrapper.write('\n')
