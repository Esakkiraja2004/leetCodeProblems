intravals = [[5,10],[6,8],[1,5],[2,3],[1,10]]

start , end  =[] , []

for l , r in intravals:
    start.append(l)
    end.append(r)

start.sort()
end.sort()

i , j =0 ,0 
g =0 
r =0

while i < len(start):

    if start[i] <= end[j]:
        i+=1
        g+=1
    else:
        j+=1
        g-=1
    r = g
print(start)
print(end)
print(r)
