s = "EPY2giL"
f = s.split(" ")
arr = [ x for x in f if x.isalnum()]
start = 0
end = len(arr) -1
while start <= end:
        arr[start],arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
print(" ".join(arr))
