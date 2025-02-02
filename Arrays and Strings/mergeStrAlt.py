word1 = 'abc'
word2 = 'pqrs'
result = []
n = max(len(word1), len(word2))
for i in range(n):
    if i < len(word1):
        result += word1[i]
    if i < len(word2):
        result += word2[i]

print(''.join(result))