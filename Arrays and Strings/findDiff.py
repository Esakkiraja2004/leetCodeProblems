arr1 =[]
arr2 =[]
nums1 = [1,2,3,3] 
nums2 = [1,1,2,2]

for i in nums1:
    if i not in nums2:
        arr1.append(i)
for i in nums2:
    if i not in nums1:
        arr2.append(i)
print([arr1,arr2])