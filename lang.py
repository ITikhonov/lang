from sys import argv

def o(x,*a):
	o.code.append(x%a)
o.code=[]

class Pos: pass

pos=Pos()

def compile_def(name,rest):
	words=rest.split()
	o("static void lang_%s(void) {",name)
	for x in words:
		o("\tlang_%s();",x)
	o("}")

def compile_c(l):
	o(l)

def compile_cdef(rest):
	name,code=rest.split(None,1)
	o("static void lang_%s(void) {",name)
	o("\t"+code)
	o("}")
	

def compile_line(l):
	t=l.split(None,1)
	if not t: return

	name,rest=t

	if name=='c': compile_c(rest)
	elif name=='cdef': compile_cdef(rest)
	else: compile_def(name,rest)

def compile_file(name):
	pos.name=name
	lines=open(name).readlines()
	for i in range(len(lines)):
		pos.line=i
		compile_line(lines[i])

def compile_all(t,l):
	for x in l:
		compile_file(x)
	open(t,'w').write("\n".join(o.code))

compile_all(argv[1],argv[2:])

