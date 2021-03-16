import numpy as np
import random

grades = np.array([[87, 96, 70], [100, 87, 90], [94, 77, 90], [100, 81, 82]])

# each row represents a student
# each col represents a Test
a = grades.sum()
b = grades.min()
c = grades.max()
d = grades.mean()
e = grades.std()
f = grades.var()
# axis can be 0 or 1
g = grades.mean(axis=0)
# print("Average of each test", g)

h = grades.mean(axis=1)
# print("Average of each student", h)

numbers = np.array([1, 4, 9, 16, 25, 36])

sqrt = np.sqrt(numbers)
# print(sqrt)

# Broadcasting example
numbers2 = np.arange(1, 7) * 10

add = np.add(numbers, numbers2)
# print(add)

multiply = np.multiply(numbers2, 5)
# print(multiply)

numbers3 = numbers2.reshape(2, 3)

numbers4 = np.array([2, 4, 6])

multiply2 = np.multiply(numbers3, numbers4)

# print(multiply2)

""" This works bc numbers4 has the same length as each row of numbers3,
so Numpy can apply the multiply operation by treating numbers4 as if it were the 
following array:
array([2, 4, 6],
      [2, 4, 6])"""


# Index and slicing
grades = np.array([[87, 96, 70], [100, 87, 90], [94, 77, 90], [100, 81, 82]])

a = grades[0, 1]
# print(a)
# 96

b = grades[1]
# array([100,87,90])

# To select multiple sequential rows, use slice
# notation ( upper limit is not included)
firsttwo = grades[0:2]  # array([[87,96,70], [100,87,90]])

# To select multiple non-sequential rows, usa a list of row indices:
grades[[1, 3]]
# array ([[100, 87, 90], [100, 81, 82]])

# All rows and only first column
c = grades[:, 0]
# If we wanted the first and the second row:
# c = grades[:2,0] because it means 0 and 1, because no upper limit included
# print(c)
# array([ 87 100  94 100])

# all rows with colums 0:2 -- ":" means all rows
d = grades[:, 0:3]
# print(d)
# array([[ 87  96  70],
# [100  87  90],
# [ 94  77  90],
# [100  81  82]])

# or specific columns using a list of column indices:
a = grades[:, [0, 2]]
# print(a)
# array([[ 87  70]
# [100  90]
# [ 94  90]
# [100  82]])


"""
Use Numpy random-number generation to create an array of twelve random grades
in the range 60 through 100, then reshape the result into a 3x4 array.
Calc the AVG of all the grades, the AVG of the grades of each test
and the AVG of the grades of each student
"""

grades = np.random.randint(60, 101, 12).reshape(3, 4)

# print(grades.mean())

# print(grades.mean(axis=0))

# print(grades.mean(axis=1))

# Shallow copies (View)
# The array method view returns a new array object with a view of the original array
numbers = np.arange(1, 6)
# array([1, 2, 3, 4, 5])

numbers2 = numbers.view()
# array([1, 2, 3, 4, 5])

numbers[1] *= 10

# print(numbers2)
# array([1, 20, 3, 4, 5])

numbers2[1] /= 10
# print(numbers)

# Slice Views
# Slices also create views. Let's make numbers2 a slice that views only the first
# three elements of numbers:

numbers2 = numbers[0:3]

numbers[1] *= 20
# print(numbers2)
# array([1, 40, 3])

# Deep copies (copy)
# The array method copy returns a new array object with a deep
# copy of the original array
numbers = np.arange(1, 6)
numbers2 = numbers.copy()

numbers[1] *= 10

# print(numbers)
# array([1, 20, 3, 4, 5])

# print(numbers2)
# array([1, 2, 3, 4, 5])


"""
The array method reshape and resize both enable you to change an array's dimensions.
Method reshape returns a view (shallow copy) of the original array with the
new dimensions. It does not modify the original array.
"""

grades = np.array([[87, 96, 70], [100, 87, 90]])

# reshape will not change the original because it is a copy
a = grades.reshape(1, 6)
# array([[87, 96, 70], [100, 87, 90]])

# resize will change the original array because its not a copy
b = grades.resize(1, 6)
# array([[87, 96, 70], [100, 87, 90]])

# Method flatten is a deep copy of the original array's data:
flattened = grades.flatten()

# alternatively, Method ravel produces a view (shallow copy) of the original array,
# which shares the grades array's data:
raveled = grades.ravel()

# confirm that they share the same data
raveled[0] = 100
raveled[5] = 99
# you get an error because there is no 7th value, so change
# raveled[6] to raveled[5]
print(grades)

# You can quickly transpose an array's rows and columns-that is "flip the array,
# so the rows become the columns and the columns become the rows
# The T attribute returns a transposed view (shallow copy) of the array

transposed = grades.T
print(transposed)

grades = np.array([[87, 96, 70], [100, 87, 90]])
grades2 = np.array([[94, 77, 90], [100, 81, 82]])

# We can combine grades and grades2 with Numpy's hstack
h_grades = np.hstack((grades, grades2))

# new array
print(h_grades)

# old array is not affected
print(grades)

# vstack
# lets assume that grades2 represents two more students' grades on three exams
v_grades = np.vstack((grades, grades2))
print(v_grades)