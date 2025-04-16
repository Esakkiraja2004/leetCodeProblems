s = "abcabc"
n = len(s)
count = {'a': 0, 'b': 0, 'c': 0}
c = 0
l = 0

for r in range(n):
    count[s[r]] += 1

    while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
        c += n - r
        count[s[l]] -= 1
        l += 1

print(c)
