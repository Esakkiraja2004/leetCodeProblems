s = "axxxxyyyyb"
part = "xy"
part_arr = [x for x in part]

stack= []

for i in s :
    stack.append(i)
    if stack[-len(part):] == part_arr:
        stack = stack[:-len(part)]
print(stack)