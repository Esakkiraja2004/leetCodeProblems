nums = [3,2,3,2,2,2]
d = {}
for i in nums:
    d[i] = nums.count(i)
                
# for count in d.values():
#     if count % 2 != 0: 
#         return False
#     return True
print(d)