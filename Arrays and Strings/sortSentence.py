s = "z1 z2 z3"
arr = s.split(" ")
d = {}
for i in arr:
    num = int(i[-1])
    d[i]= num
sorted_words = sorted(d.keys(), key=d.get)

sorted_sentence = " ".join(word[:-1] for word in sorted_words)

print(sorted_sentence)
