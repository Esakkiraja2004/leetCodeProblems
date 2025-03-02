nums = [1,3,4,2,3]
seen = set()
for i in nums:
    if i in seen:
        print(i)
        break
    else:
        seen.add(i)