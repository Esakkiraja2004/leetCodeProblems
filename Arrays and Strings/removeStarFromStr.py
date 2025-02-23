s = "erase*****"
stack = []
for c in s :
    if stack and c == "*":
        stack.pop()
    else:
        stack.append(c)
print("".join(stack))

