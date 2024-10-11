a ="qwertyuiop"
b = "asdfghjkl"
c = " zxcvbnm"
arr_a = [x for x in a ]
arr_b = [x for x in b ]
arr_c = [x for x in c ]

words = ["Hello","Alaska","Dad","Peace"]

arr =[]

for x in words:
    word = x.lower()
    c =set(word)
    if c.issubset(set(arr_a)) :
        arr.append(x)
    elif c.issubset(set(arr_b)):
        arr.append(x)
    elif c.issubset(set(arr_c)):
        arr.append(x)
print(arr)

