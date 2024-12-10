a = "ababccc"
arr = set()
for i in range(len(a)):
    for j in range(i+1, len(a)):
        m = a[i:j]
        arr.add(m)
l = [x for x in arr ]
print(l)