from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        visited_accounts=[False]*len(accounts)
        email_accounts_map=defaultdict(list)
        res=[]

        #그래프 구축
        for i,account in enumerate(accounts):
            for j in range(1,len(account)):
                email=account[j]
                email_accounts_map[email].append(i)

        #dfs함수
        def dfs(i,emails):
            if visited_accounts[i]:
                return
            visited_accounts[i]=True
            for j in range(1,len(accounts[i])):
                email=accounts[i][j]
                emails.add(email)
                for neighbor in email_accounts_map[email]:
                    dfs(neighbor, emails)
        #실행!
        for i, account in enumerate(accounts):
            if visited_accounts[i]:
                continue
            name, emails=account[0],set()
            dfs(i, emails)
            res.append([name]+sorted(emails))

        return res

        