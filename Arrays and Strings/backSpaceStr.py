s ="y#fo##f"
t ="y#f#o##f"

sArr = []
tArr= []

for i in s:
    if sArr and i == "#":
        sArr.pop()
    elif i != "#":
        sArr.append(i)

for i in t:
    if tArr and i == "#":
        tArr.pop()
    elif i != "#":
        tArr.append(i)

print(sArr)
print(tArr)

print("".join(sArr) == "".join(tArr))