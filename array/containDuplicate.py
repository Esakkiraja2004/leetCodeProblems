a = [1,2,3,1,2,3]
k = 2
l = 0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] == a[j]:
            l = j - i
            print(f"Indices: {i}, {j}")  
            break
print(l)
if l <= k and len(a) >= l:
    print(True)
else:
    print(False)