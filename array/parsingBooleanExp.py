e = "&(|(f))"
arr = [x for x in e]
boo =  [y  for y in arr if y == 't' or y == 'f']
exp = [x for x in arr if x == '!' or x == '|' or x == '&' ]
while exp :
    op = exp.pop()
    if op == '|':
        while boo :
            