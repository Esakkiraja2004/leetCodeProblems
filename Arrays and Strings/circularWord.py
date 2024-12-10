sentence ="ab a a"
arr = sentence.split(" ")
res = True
if len(arr) == 1  and sentence[0] == sentence[-1]:
        res =True
if arr[0][-1] != arr[-1][-1]:
    res = False
for i in range(len(arr)):
    for j in range(i+1 ,len(arr)):
        if arr[i][-1] != arr[j][0]:
            res = False
            break
        else:
            res =  True
print(arr)
print(res)
            
            
