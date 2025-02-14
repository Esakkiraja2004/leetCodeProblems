s = "b"
arr = []
res =[]
for i in s:
    if i not in arr :
        arr.append(i)
    else :
        res.append(len(arr))
        arr =[]
        arr.append(i)
        continue

# print(arr)
# print(h)
print(res)
