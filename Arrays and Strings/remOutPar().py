s = "(()())(())"
res = []
count = 0
for c in s:
    if c == "(":
        if count > 0:  # Ignore outermost '('
            res.append(c)
        count += 1
    elif c == ")":
        count -= 1
        if count > 0:  # Ignore outermost ')'
            res.append(c)
print("".join(res))