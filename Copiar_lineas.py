b=input("Introduce el nombre del archivo a copiar: ")
fh = open(b,"r")
a=input("Introduce el nombre del archivo destino: ")
fs = open(a,"w")
line = fh.readline()
while line:
	c=line.split()
	if c[1].upper:
		fs.write(line)
	line= fh.readline()
fh.close()