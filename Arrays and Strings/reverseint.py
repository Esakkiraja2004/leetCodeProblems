x = -123
arr = list(str(x))
s = 0
e = len(arr)-1
while s <= e:
    if arr[s].isdigit() == False:
        s+=1
    else:
        arr[s],arr[e] = arr[e],arr[s]
        s+=1
        e-=1
print(int(''.join(arr)))