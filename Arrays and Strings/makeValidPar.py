s = ")))))"
open_brac , close_brac = 0 ,0 
for x in s:
    if x == "(":
        open_brac += 1
    else:
        if open_brac > 0:
            open_brac -= 1
        else:
            close_brac += 1
print(open_brac + close_brac)
