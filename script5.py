import sys

f1=open(sys.argv[1],'r')
f2=open(sys.argv[2],'w')
w=f1.readline()
while w:

	f2.write(w)
	w=f1.readline();
f1.close()
f2.close()
