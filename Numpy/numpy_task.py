import numpy as np
#Task : 1

"""
Create this array using NumPy:

 [[5,10,15],
 [20,25,30]]

Print:

shape
ndim
dtype
size

Task 2
- Create an array from 0 to 20 with step 2.

Task 3
- Create a 3x3 matrix of ones.

Task 4
- From this array:[10,20,30,40,50]

Slice to get:
[20,30,40]
"""
x = np.array([[5,10,15],[20,25,30]])
#print(x, x.shape,x.ndim,x.dtype,x.size)

print(np.arange(0,20,2))
print(np.zeros((3,3)))
arr = np.array([10,20,30,40,50])
print(arr[1:4])

"""
Task 1

Create arrays

a = [2,4,6]
b = [1,3,5]

Compute

addition
subtraction
multiplication

Task 2

Create array : [1,4,9,16]
Compute :square root log

Task 3

For matrix
[[10,20,30],
 [40,50,60]]

Find

sum of entire matrix
column sum
row sum
"""

a = np.array([2,4,6])
b = np.array([1,3,5])
print(a+b,a*b,a-b)

root = np.array([1,4,9,13])
print(np.sqrt(root),np.log(root),np.sum(root))

matrix1 = np.array([[10,20,30], [40,50,60]])
print(np.sum(matrix1,axis = 0),np.sum(matrix1,axis = 1),np.sum(matrix1))