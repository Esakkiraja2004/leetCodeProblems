num = "10200"
k = 1
stack =[]

for c in num:
    while k > 0 and stack and stack[-1] > c:
        k -= 1
        stack.pop()
    stack.append(c)
stack = stack[:len(stack)-k]
res = "".join(stack)
print(str(int(res))) if res else "0"