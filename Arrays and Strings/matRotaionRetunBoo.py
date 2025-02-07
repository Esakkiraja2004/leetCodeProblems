mat = [[0,1],[1,1]]
target = [[1,0],[0,1]]

mat_arr = []
tar_arr = []


for i in range(len(mat)):
        mat_arr.append(mat[i])
        tar_arr.append(target[i])

print(mat_arr)
print(tar_arr)

if mat_arr.count(1) == tar_arr.count(1) and mat_arr.count(0) == tar_arr.count(0):
    print(True)
else:
    print(False)