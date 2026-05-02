import numpy as np

# Input matrices
print("Enter Matrix A:")
matrix_a = np.array([list(map(int, input().split())) for i in range(3)])

print("Enter Matrix B:")
matrix_b = np.array([list(map(int, input().split())) for i in range(3)])


madd=matrix_a+matrix_b
print("Addition (A + B):")
print(madd)

msub=matrix_a-matrix_b
print("Subtraction (A - B):")
print(msub)

mmul=matrix_a*matrix_b
print("Element-wise Multiplication (A * B):")
print(mmul)

mdot=np.dot(matrix_a,matrix_b)
print("A dot B:")
print(mdot)

Mtran=matrix_a.T
print("Transpose of A:")
print(Mtran)
