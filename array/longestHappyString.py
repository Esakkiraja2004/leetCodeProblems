a = 1
b = 1
c = 7
arr_large =[a,b,c]
r =[]

    if a > b and a > c and r[-2] != 'a':
        r.append('a')
    elif b > a and  b > c and r[-2] != 'b':
        r.append('b')
    elif r[-2] != 'c':
        r.append('c')
print(r)

