s = "cb34"

arr = [x for x in s]  # Convert string to list

i = 1
while i < len(arr):  # Use while loop instead of for loop to safely modify list
    if arr[i-1].isalpha() and arr[i].isalpha():
        i += 1
        continue
    else:
        arr.pop(i)  # Remove current element
        arr.pop(i-1)  # Remove previous element
        i = max(1, i - 1)  # Reset index to avoid skipping elements

print(arr)
