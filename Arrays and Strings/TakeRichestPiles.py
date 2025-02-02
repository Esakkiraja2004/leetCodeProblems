import math
gifts = [25,64,9,4,100]
k = 4
while k:
    gifts.sort(reverse=True)
    pils = gifts[0]
    gifts.pop(0)
    gifts.append(int(math.sqrt(pils))) 
    k-=1
print(sum(gifts))
