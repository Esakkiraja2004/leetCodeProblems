n = len(nums)
curr_sum = sum(nums[:k]) 
max_avg = float(curr_sum) / k 

for i in range(k, n):
    curr_sum += nums[i] 
    curr_sum -= nums[i - k]
    avg = float(curr_sum) / k 
    max_avg = max(avg, max_avg)
        
return max_avg