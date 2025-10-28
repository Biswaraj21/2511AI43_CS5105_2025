def brute(arr):
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    max_money = 0
    total_combinations = 1 << n 
    for mask in range(total_combinations):
        valid = True
        total = 0
        for i in range(n):
            if (mask >> i) & 1:  
                if i > 0 and ((mask >> (i - 1)) & 1):
                    valid = False
                    break
                if i == 0 and (mask >> (n - 1)) & 1:
                    valid = False
                    break
                total += arr[i]
        if valid:
            max_money = max(max_money, total)
    return max_money

def linear(houses):
    if not houses:
        return 0
    n=len(houses)
    if n==1:
        return houses[0]
    prev2=0
    prev1=houses[0]
    for i in range(1,n):
        curr=max(prev1,prev2+houses[i])
        prev1,prev2=curr,prev1
    return prev1

def optimal(houses):
    if not houses:
        return 0
    if len(houses)==1:
        return houses[0]
    return max(linear(houses[:-1]),linear(houses[1:]))


houses = list(map(int,input("Enter houses: ").split()))
print("Brute: ",brute(houses))
print("Optimal: ",optimal(houses))