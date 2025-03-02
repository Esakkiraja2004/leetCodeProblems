nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

s = sorted(nums1)
s2 = sorted(nums2)

i = 0
j = 0
output = []

while i < len(s) and j < len(s2) :
    if s[i] < s2[j]:
        i+=1
    elif s[i]  > s2[j]:
        j+=1
    else:
        output.append(s[i])
        i+=1
        j+=1

print(output)