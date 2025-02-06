nums =[1,0,1,1]
k = 1
hashmap ={}

for i , num in enumerate(nums):
    print(i , num)
    if num in hashmap :
        if abs(i - hashmap[num]) <= k:
            print(True)
    hashmap[num] = i
print(hashmap)