nums = [1,2,3,1]
rob1 , rob2 = 0, 0 
res = 0
for i in nums:
    temp = max(i + rob1, rob2)
    rob1 = rob2
    rob2  = temp
    res= rob2
print(res)

