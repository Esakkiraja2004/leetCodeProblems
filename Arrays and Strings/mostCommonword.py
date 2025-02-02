paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned =["hit"]
p =  paragraph.split()
arr = [ x.lower() for x in p  ]
arr.sort()
c =[]
for i in arr:
    c.append(arr.count(i))
print(c)
