nums =[6,10,6]
c = nums[0]
ans = nums[0]
for i in range(1,len(nums)):
    if nums[i-1] < nums[i]:
        print(" Current value : " ,nums[i-1] , nums[i])
        c =+nums[i-1]
    else:
        c = nums[i]
    ans = max(c , ans)

print(ans)