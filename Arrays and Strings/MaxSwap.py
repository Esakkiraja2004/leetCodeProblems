num = '2736'
# sorted_arr = ['7', '6', '3', '2']

arr = [x for x in num]

# Create a sorted version of the array to compare
sorted_arr = sorted(arr, reverse=True)

# Loop through the array and swap the first mismatch
for i in range(len(arr)):
    if arr[i] != sorted_arr[i]:
        # Find the rightmost occurrence of the larger digit in the original array
        for j in range(len(arr)-1, i, -1):
            if arr[j] == sorted_arr[i]:
                # Swap the digits
                arr[i], arr[j] = arr[j], arr[i]
                break
        break

# Convert back to integer
res = int(''.join(arr))
print(res)
