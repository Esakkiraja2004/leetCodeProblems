s = "is2 sentence4 This1 a3"
arr = s.split(" ")
d = {}
for i in arr:
    c = i[:-1]
    d[c] = int(i[-1])
sorted_words = sorted(d.keys(), key=d.get)

sorted_sentence = " ".join(word[:-1] for word in sorted_words)

print(sorted_sentence)