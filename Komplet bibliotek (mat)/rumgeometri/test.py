from rumgeom import Matrix, Vector

a1 = Vector([3, -2, 1, 4])
# a2 = Vector([1, 0, 2, 6])
# a3 = Vector([4, 1, 2, 9])


# b1 = Vector([1, -3, 2])
# b2 = Vector([0, 1, -4])
# b3 = Vector([2, -4, 1])

A = Matrix([a1])
# B = Matrix([b1, b2, b3])

# print(f'Dette er A: \n{A}')
# print(f'Dette er B: \n{B}')



# print(f'Dette er Matrix A og B multipliceret: \n{B*A}')


#print(f'Iden af A: {Matrix.identity_matrix(4)}')
# print(f'Add col: {Matrix.identity_matrix(4).append_column(Vector([2, 3, 4, 4]))}')
# print(f'Gauss of A: \n{A.gauss()}')
print(f'Dette er A{A}')
print(f'Dette er A transposed{A.transpose()}')