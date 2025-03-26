command =  "(al)G(al)()()G"
arr = []
for i in range(len(command)):
    if command[i] == "(" and command[i+1] == ")":
        arr.append("o")
    elif command[i].isalpha():
        arr.append(command[i])
print("".join(arr))