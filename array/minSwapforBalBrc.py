a = "][]["
close , maxClose =0 ,0
for x in a :
    if x == "[":
        close -=1
    else:
        close +=1
        maxClose  = max(close, maxClose)

print(maxClose)
