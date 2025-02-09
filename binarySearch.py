def search (target , arr):
    low =0
    high = len(arr)-1
    mid = 0
    while low <=  high:
        mid = high + low // 2
        if arr[mid] < target:
            low = mid+1
        elif arr[mid] > target:
             high = mid -1
        else:
            return mid
    return -1
arr = [4,5,6,7,0,1,2]
target = 0
print(search(target,arr))

