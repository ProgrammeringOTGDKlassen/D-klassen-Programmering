from mat.rumgeom import Matrix, Vector

#Matrix([])

a1 = Vector([3, -2, 1, 4])
# a2 = Vector([1, 0, 2, 6])
# a3 = Vector([4, 1, 2, 9])

b1 = Vector([3, 2, 1, -5, 10])
b2 = Vector([-3, 2, 5, 1, 6])
b3 = Vector([-5, 7, 1, 9, 9])
b4 = Vector([23, 4, 1, 12, 3])

print(str(b4.normalize()))

A = Matrix([a1])
B = Matrix([b1, b2, b3, b4])

# print(f'Dette er A: \n{A}')
# print(f'Dette er B: \n{B}')



# print(f'Dette er Matrix A og B multipliceret: \n{B*A}')

res, inverse, elementaries = B.gauss()

print(f'Gauss af B: \nResult: \n{str(res)} \n\nInverse: \n{str(inverse)} \n\n {str(elementaries)}')

#print(f'Iden af A: {Matrix.identity_matrix(4)}')
# print(f'Add col: {Matrix.identity_matrix(4).append_column(Vector([2, 3, 4, 4]))}')
# print(f'Gauss of A: \n{A.gauss()}')
#print(f'Dette er A{A}')
#print(f'Dette er A transposed{A.transpose()}')