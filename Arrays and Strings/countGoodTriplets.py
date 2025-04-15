arr = [3,0,1,1,9,7]
a = 7
b = 2
c = 3

res = []

count = 0

for i in range(len(arr)):
    for j in range(len(arr)):
        for k in range(len(arr)):
            if 0 <= i and i < j and j < k and k < len(arr) and  abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k])<= c:
                res.append([arr[i],arr[j],arr[k]])
                count+=1
print(res)
print(count)