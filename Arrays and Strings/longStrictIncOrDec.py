nums =[3,2,1]
increment =1
decrement =1
max_len = 1
for i in range(1 , len(nums)):
        print(nums[i],nums[i-1])
        if nums[i] > nums[i-1]:
            increment += 1
            decrement = 1
        elif nums[i] < nums[i-1]:
            decrement += 1
            increment = 1            
        else:
             increment , decrement = 1 , 1
        max_len = max(increment,decrement)

print("increament: " , increment)
print("decrement: " , decrement)
print(max(increment , decrement ))