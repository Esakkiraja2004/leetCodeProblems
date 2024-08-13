m = [[1,2,3],[4,5,6],[7,8,9]]
res = []
for i in range(len(m[0])):
    temp = []
    for j in range(len(m)):
        temp.append(m[j][i])
    res.append(temp)
# print(res[2][0])
print(m[2][0])