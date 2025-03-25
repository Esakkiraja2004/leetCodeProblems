s = "abciiidef"
arr = ["a", "e", "i", "o", "u"]
k = 3

l = 0
m = 0
count = 0

for r in range(len(s)):
    if s[r] in arr:
        count += 1
    
    if r - l + 1 > k:
        if s[l] in arr:
            count -= 1
        l += 1

    if r - l + 1 == k:
        m =max(count , m)

print(m)
