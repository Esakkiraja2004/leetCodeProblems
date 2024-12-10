grid =[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

p = 0

c =0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 1:
            c +=1
        if c > 1:
            if c  == 2:
                p +=5
            elif c == 3:
                p+= 6
            elif c == 4:
                p+= 8
        elif c == 1:
            p+=4
            c =0
print(p)


