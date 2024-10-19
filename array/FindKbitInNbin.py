n = 3
k =1 
arr =[]
for x in bin(n):
    if x == 'b':
        continue
    arr.append(x)
res = [ i for i in range(len(arr)) if i == k ]
print(res)