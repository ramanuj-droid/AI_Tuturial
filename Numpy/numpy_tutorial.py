import numpy as np

#N-D Array
x = np.array([1,2,3,4,5,6])
matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])


#Types-Array

zero = np.zeros((3,3))
ones = np.ones((3,3))
collection = np.arange(0,10,2)
lin = np.linspace(0,1,5)

#Attributes of Array
"""
print(matrix.shape)  #Shape - dimension of array
print(matrix.ndim) #To find dimensions
print(matrix.dtype) #To find datatype
print(matrix.size) # to find length
"""
#Slicing - NumPy slicing often returns views, not copies.

sliced = x[1:4]

arr = np.array([1,2,3,4])
slice_arr = arr[1:3]
slice_arr[0] = 100

#Element - Wise Operation

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

#print(arr1+arr2, arr1-arr2,arr1*arr2)

"""
Each element is added individually.

1 (+-*) 4
2 (+-*) 5
3 (+-*) 6

"""

#Scalar Opearation

a = np.array([10,20,30])
#rprint(a+10,a*2,a/10,a-5)

#Vectorization (Why NumPy is Fast)

v = [1,4,5,6]

#for i in v: result.append(i*2) print(result) ==> print(v*2)

#Mathematical Functions

root = np.array([1,4,9,13])
#print(np.sqrt(root),np.log(root),np.sum(root)) #std,var,etc

#Axis Concept

a = np.array([[1,2,3],[4,5,6]])
#print(np.sum(a ,axis =1))

#BroadCasting
"""
Broadcasting allows NumPy to perform operations on arrays of different shapes without explicitly copying data.
Broadcasting Rules (Important)-Two arrays are compatible if:

Rule 1 : Dimensions are equal
or
Rule 2 : One dimension is 1
"""
temp = np.array([1,2,3])
f = 3

matrix2 = np.array([[1,2,3],[4,5,6]])
vector = np.array([10,20,30])

col_matrix = np.array([[1,2,3],[4,5,6]])
column = np.array([[10],[20]])

"""print(col_matrix + column)
   print(matrix2 + vector)
"""

#Linear Algebra with Numpy

#Matrix Multiplication 

#np.dot(matrix2,matrix2)

"""
print(matrix2*matrix2)
print(matrix.T) #transpose
print(np.linalg.det(matrix)) #transpose
print(np.linalg.inv(matrix2)) #determinant

A = np.array([
    [4,2],
    [1,3]
])

values, vectors = np.linalg.eig(A)

print(values)
print(vectors)
"""

#Boolean Masking

ex = np.array([10,20,30,40,50])
#mask = ex>25
#print(ex[ex>15])

result_multiple = arr[(arr > 10) & (arr < 30)]
"""
&   → AND
|   → OR
~   → NOT

data = np.array([18,22,25,17,30,16])
data[data < 18] = 18

"""

#RANDOM MODULE

print(np.random.rand(5),np.random.rand(3,3),np.random.randint(0,10,5))

#Random distribution
print(np.random.randn(5))

choose = np.array([10,20,30,40])
print(np.random.choice(choose))