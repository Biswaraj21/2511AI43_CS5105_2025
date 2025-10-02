from collections import defaultdict

def optimal(nums, k):
    freq = defaultdict(int)
    prefixXor = 0
    count = 0
    for num in nums:
        prefixXor ^= num
        if prefixXor == k:
            count += 1
        if (prefixXor ^ k) in freq:
            count += freq[prefixXor ^ k]
        freq[prefixXor] += 1
    
    return count

nums = [4, 2, 2, 6, 4]
k = 6
print(optimal(nums, k))  