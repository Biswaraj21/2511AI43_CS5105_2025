def brute(account):
    changes=True
    while changes:
        changes=False
        used=[False]*len(account)
        new_accont=[]
        for i in range(len(account)):
            if used[i]:
                continue
            name,*emails1=account[i]
            emails1=set(emails1)
            for j in range(i+1,len(account)):
                if used[j]:
                    continue
                _,*emails2=account[j]
                emails2=set(emails2)
                if emails2 & emails1:
                    emails1|=emails2
                    used[j]=True
                    changes=True
            new_accont.append([name]+sorted(list(emails1)))
            used[i]=True    
        account=new_accont
        return account
    
class DSU:
    def __init__(self):
        self.parent={}
    def find(self,x):
        if x not in self.parent:
            self.parent[x]=x
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        self.parent[self.find(x)]=self.find(y)

def optimal(accounts):
    dsu=DSU()
    account_to_name={}
    for account in accounts:
        name=account[0]
        first_email=account[1]
        for email in account[1:]:
            dsu.union(first_email,email)
            account_to_name[email]=name
    group={}
    for email in account_to_name:
        root=dsu.find(email)
        if root not in group:
            group[root]=[]
        group[root].append(email)
    result=[]
    for root,email in group.items():
        result.append([account_to_name[root]]+sorted(email))
    return result
    
accounts = [
  ["John", "johnsmith@mail.com", "john00@mail.com"],
  ["John", "johnnybravo@mail.com"],
  ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
  ["Mary", "mary@mail.com"]
]

print("Brute Force:", brute(accounts))
print("Optimal:", optimal(accounts))