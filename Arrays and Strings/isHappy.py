n = 19
seen = []
while n != 1 and n not in seen:
    seen.append(n)
    n = sum(int(digit) ** 2 for digit in str(n))
res = n == 1
print(seen)
print(res) 
 