from sys import argv

def compiler(code):
	compiler.func(code)

def setcompiler(func):
	compiler.func=func



###############################################################

def default(code):
	print('default')

def interpret(code):
	w=code.word()
	macro.all.get(w,compile)(code,w)

def compile(code,w):
	print("	%s();"%(w,))
	

###############################################################

def macro(x):
	if x.__doc__:
		macro.all[x.__doc__]=x
	else:
		macro.all[x.__name__[1:]]=x
macro.all={}


@macro
def mcolon(code,w):
	":"
	w=code.word()
	print("void %s(void) {"%(w,))

@macro
def msemicolon(code,w):
	";"
	print("}")

###############################################################

setcompiler(interpret)

class EOF(Exception):
	pass

def word(f):
	word=""
	x=' '
	while x==' ':
		x=f.read(1)
		if not x:
			raise(EOF)
		if x=='\n':
			f.lineno+=1
			x=' '

	while x!=' ':
		word=word+x
		x=f.read(1)
		if not x: break
		if x=='\n':
			f.lineno+=1
			x=' '
	return word
	

def compile_file(name):
	code=open(name)
	code.word=lambda: word(code)
	code.lineno=1

	try:
		while True:
			compiler(code)
	except EOF:
		pass

compile_file(argv[1])

