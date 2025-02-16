num = 3749
hmap = {
      1:    'I',
      4:    'IV',
      5:    'V',
      9:    'IX',
     10:    'X',
     40:    'XL',
     50:    'L',
     90:    'XC',
    100:    'C',
    400:    'CD',
    500:    'D',
    900:    'CM',
   1000:    'M'
}

arr = []
keys = sorted(hmap.keys() ,  reverse= True)  # Sort keys in descending order

for k in keys:
    while num >= k:
        arr.append(hmap[k])
        num -= k

print("".join(arr))  