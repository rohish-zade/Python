# https://www.hackerrank.com/challenges/np-dot-and-cross/problem?isFullScreen=true

import numpy as np

n = int(input())

a_integers = []
b_integers = []

for _ in range(n):
    temp = input().split()
    temp_list = list(map(int, temp))
    a_integers.append(temp_list)

for _ in range(n):
    temp = input().split()
    temp_list = list(map(int, temp))
    b_integers.append(temp_list)

# print(a_integers)
array_a = np.array(a_integers)
array_b = np.array(b_integers)

# Method 1: Using numpy.matmul()
result_c = np.matmul(array_a, array_b)

# Method 2: Using @ operator
result_d = array_a @ array_b

# Method 3: Using numpy.dot()
result_e = np.dot(array_a, array_b)

print(result_c)