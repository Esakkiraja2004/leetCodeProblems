n = [0,1]
n.sort()

if n[0] != 0 :
    print(0)

if n[-1] != len(n):
    print(len(n))
    
for i in range(0,len(n)):
    if n[i]!= i:
        print(i)