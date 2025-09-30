def optomal(nums):
    prefix_sum=0
    seen={}
    max_len=0
    for i,num in enumerate(nums):
        prefix_sum+=num
        if prefix_sum==0:
            max_len=i+1
        elif prefix_sum in seen:
            max_len=max(max_len,i-seen[prefix_sum])
        else:
            seen[prefix_sum]=i
    return max_len

arr = [15, -2, 2, -8, 1, 7, 10, 23]
#print("Brute:", longestZeroSumBrute(arr))
print("Optimal:", optomal(arr))