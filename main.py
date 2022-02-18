# 1. Import the numpy package under the name `np`
import numpy as np

##### DECLARING NUMPY ARRAYS #####

# 2. Use np.array(<list>) to convert the list below into a numpy array. The array should be saved in a variable. Then print both the list and the array.
a = [300, -200, 100, 0, -100, 200, -300]
b= np.array(a)

## The array method in numpy has an optional dtype argument which specifies the datatype each element should be. For the array above, it could be implemented using A = np.array(a, dtype=str) ##

# 3. Declare new arrays with different datatypes using the list from #2. Datatypes to use: str, float, np.int32, np.int8, np.uint32, up.uint8.
b= np.array(a,dtype=str)
b2= np.array(a,dtype=float)
b3= np.array(a,dtype=np.int32)
b4= np.array(a,dtype=np.int8)
b5= np.array(a,dtype=np.uint32)
b6= np.array(a,dtype=np.uint8)
# 4. Use np.zeros(<int>) to create a array of zeroes of size 10. This should be saved in a variable. Then print the array.

c=np.zeros(10)
print(c)
# 5. In your array of zeroes, change the fifth 0 to a 6. (remember how indexing works in lists?) Print the array.

c[5]=6
print(c)
# 6. Use np.arange(<int>, <int>) to create an array with values ranging from 11 to 46. Print the array.

d=np.arange(10, 46)
print
# 7. Reverse the array you created in #6. Print the array.

e=np.arange(46,11)


# 8. Use <array>.reshape(<int>, <int>) to turn your array from #6 into a multidimensional 6x6 array. Print the array.

f=d.reshape(6,6)
print(f)
# 9. Use np.random.random((<int>, <int>)) to create a 10x10 array with random values. Print the array.

g=np.random.random((1,2))
print(g)

# 10. Use np.random.randint(<int>, <int>, size=(<int>, <int>)) to create a 3x3 array with random integers. Print the array.

h=np.random.randint(31,44,size=(3,3))
print(h)

# 11. Use <array>.max() and <array>.min to identify the maximums and minimums of the arrays you created in #9 and #10. Print the results.
x=g.max()
y=h.min()
x1=h.max()
y1=g.min()

print(x,y,x1,y1)
# 12. Use <array>.mean() to find the means of the two arrays you created in #9 and #10. Print the results.

z=g.mean()
z1=h.mean()
print(z,z1)
# 13. Convert the following two lists into 2X3 arrays. (You will need to use np.array and .reshape)

a = [2, 3, 5, 7, 11, 13]
b = [3, 1, 4, 1, 5, 9]
j=np.array(a)
k=np.array(b)
j1=j.reshape(2,3)
k1=k.reshape(2,3)
# 14. Add the two arrays from #13 (<array> + <array>)
l=j1+k1


# 15. Multiply both arrays from #13 by 10.

n=10*k1
m=10*j1