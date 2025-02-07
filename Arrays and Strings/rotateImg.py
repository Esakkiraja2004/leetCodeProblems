matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix.reverse()
arr = [[0]*len(matrix) for i in range(len(matrix))]

for i in range(len(matrix)):
    for j in range(len(matrix_two)):
        arr [i][j], arr[j][i] = matrix [j][i] , matrix[i][j]
print(arr)