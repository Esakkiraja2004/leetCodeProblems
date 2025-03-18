candies = [2,3,5,1,3]
extraCandies = 3
arr =[]
for i in candies:
    if i+extraCandies >= max(candies):
        arr.append(True)
    else:
        arr.append(False)
print(arr)