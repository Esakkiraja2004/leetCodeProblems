l1 = ["Shogun","Tapioca Express","Burger King","KFC"]
l2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]

common = set(l1) & set(l2)

ind ={}

for i ,j in enumerate(l1):
    if j in common:
        ind[j] = i
for i ,j in enumerate(l2):
    if j in common:
        ind[j] += i
min_s = min(ind.values())
print([i for i ,j in ind.items() if j == min_s])