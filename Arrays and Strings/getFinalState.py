nums = [2,1,3,5,6] 
k = 5 
multiplier = 2
while k > 0:
    mini = min(nums)
    mini_index = nums.index(mini)
    nums.insert(mini_index , mini * multiplier)
    nums.pop(mini_index + 1)
    k -= 1
print(nums)