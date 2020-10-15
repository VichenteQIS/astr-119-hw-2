import numpy as np #import numpy

#integers
i = 10 #integer
print("The data type of i is",type(i)) #print out the data type of 1

a_i = np.zeros(i,dtype=int) #declare an array of ints
print("The data type of a_i is",type(a_i)) #np.ndarray
print("The data type of a_i[0] is",type(a_i[0])) #int64

#floats

x = 119.0 #floating point number
print("The type of x is ",type(x)) #print out the data type of x

y = 1.19e2 #float 119 in scientific notation
print("The type of y is ",type(y)) #print out the data type of y

z = np.zeros(i,dtype=float) #declare array of floats
print("The type of z is ",type(z))				#will return nd array
print("The type of z[0] is ",type(z[0]))			#will retrunr float64

d = np.zeros((2,2),dtype=(float))
d[0,0] = 1.0
d[1,1] = 1.0
print(d)