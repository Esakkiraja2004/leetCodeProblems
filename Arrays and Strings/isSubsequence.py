s = "abc"
t = "ahbgdc"


i = 0
j = 0

arr =[]

while i < len(s) and j < len(t):
    if s[i] == t[j]:
        i += 1
        j += 1
       
    else:
        j+=1
if i == len(s):
    print(True)
