s = ["h","e","l","l","o"]
l = len(s)
e = l -1
d =0 
while d < e:
    s[e], s[d] = s[d], s[e]
    d+=1
    e-=1
print(s)