

n1 = [1,2,3]
n2 = [3,2,4,2]

arr =[]

for i in range(len(n1)):
    for j in range(len(n2)):
        if n1[i] == n2[j]:
            arr.append(n1[i])

print(arr)

res = set(arr)
print(list(res))


        # set1 = set(nums1)
        # set2 = set(nums2)

        # return list(set1.intersection(set2))