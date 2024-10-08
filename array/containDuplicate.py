a = [13,23,1,2,3]
a.sort()
k = 5
l = 0
s =set(a)
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] == a[j]:
            l = j - i
            print(f"Indices: {i}, {j}")  
            break
print(l)
if l <= k and len(a) >= l  and a != list(s) :
    print(True)
else:
    print(False)
