s = "a-bC-dEf-ghIj"
a_l = list(s)
start = 0
end = len(s) -1
while start <= end:
    if a_l[start].isalpha() and a_l[end].isalpha():
        a_l[start],a_l[end] = a_l[end],a_l[start]
        start += 1
        end -= 1
    elif a_l[start].isalpha() and a_l[end].isalpha() == False:
        end -= 1
    else:
        start += 1
print("".join(a_l))