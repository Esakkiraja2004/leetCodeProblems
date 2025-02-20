s = "abca"
arr = list(s)
start = 0
end = len(s) - 1
c = 0

while start <= end:
    if s[start] == s[end]:
        start += 1
        end -= 1
    else:
        # Try removing one character
        left_skip = arr[start+1:end+1]  # Remove left character
        right_skip = arr[start:end]  # Remove right character
        
        if left_skip == left_skip[::-1] or right_skip == right_skip[::-1]:
            c += 1  # One removal allowed
        else:
            c += 2  # More than one removal needed

        break  # Stop checking further

# If at most one removal was needed
print(c <= 1)

