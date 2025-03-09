s = "aababcabc"
sett = set()
l = 0
n = len(s)

count = 0

for r in range(n):
    if(r-l)+1 > 3:
        l+=1
    sett.add(s[r])
    if (r-l)+1 == 3 and len(set(s[l:r+1])) == 3:
        count+=1 
    
print(count)


