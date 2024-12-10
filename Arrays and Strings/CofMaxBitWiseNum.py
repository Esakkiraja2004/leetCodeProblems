from collections import Counter
nums =[3,2]
dp = Counter([0])
max_or = 0
for num in nums:
    for val, count in list(dp.items()):
        dp[val | num] += count
        max_or |= num

print(dp[max_or])