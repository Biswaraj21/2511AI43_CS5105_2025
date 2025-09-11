def brute(stocks):
    n=len(stocks)
    max_profit=0
    for i in range(n-1):
        for j in range(i,n):
            max_profit=max(max_profit,stocks[j]-stocks[i])
    return max_profit

def optimal(stocks):
    n=len(stocks)
    min_buy=float('inf')
    max_profit=0
    for i in range(n):
        min_buy=min(min_buy,stocks[i])
        max_profit=max(max_profit,stocks[i]-min_buy)
    return max_profit

if __name__=='__main__':
    stocks=input('Enter stock proces: ').split()
    stocks=list(map(int,stocks))
    print('Brute: ',brute(stocks))
    print('optimal: ',optimal(stocks))