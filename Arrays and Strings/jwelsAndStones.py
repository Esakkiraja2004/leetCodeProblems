jewels = 'aA'
stones = "aAAbbbb"

arr_j = list(jewels)
arr_s = list(stones)

c= 0

for i in range(len(arr_j)):
    if arr_j[i] in arr_s:
        c+= arr_s.count(arr_j[i])
print(c)