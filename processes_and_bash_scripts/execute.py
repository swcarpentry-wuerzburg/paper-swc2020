# Use python to run the echo.sh script with command line inputs specified in
# numpy
# Introduction to the subprocess module

import subprocess
import numpy

table = numpy.array([[2,2.5],[3,4.5]])
n = table.shape[0]

for i in range(n):
	p = subprocess.Popen(["./echo.sh",str(table[i,0]),str(table[i,1])],\
 		stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	stdout, stderr = p.communicate()
	print(stdout)
	print(stderr)
