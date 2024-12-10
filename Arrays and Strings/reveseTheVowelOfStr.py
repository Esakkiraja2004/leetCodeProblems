g = 'IceCreAm'
s = list(g)

v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

# Find the indices of vowels
vowel_indices = [i for i in range(len(s)) if s[i] in v]

# Reverse the vowels at these positions
start, end = 0, len(vowel_indices) - 1

while start < end:
    s[vowel_indices[start]], s[vowel_indices[end]] = s[vowel_indices[end]], s[vowel_indices[start]]
    print(s[vowel_indices[start]] , " SWAP" , s[vowel_indices[end]])
    start += 1
    end -= 1

# Join the list back into a string
result = ''.join(s)
print(result)
print(vowel_indices)

# g = 'IceCreAm'
# v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

# # Extract the vowels in reverse order
# vowels = [char for char in g if char in v][::-1]

# # Replace vowels in the original string with the reversed vowels
# result = []
# vowel_index = 0

# for char in g:
#     if char in v:
#         result.append(vowels[vowel_index])
#         vowel_index += 1
#     else:
#         result.append(char)

# # Join the result to form the final string
# result = ''.join(result)
# print(result)
