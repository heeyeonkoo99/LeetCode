class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank_set=set(bank)
        if end not in bank_set:
            return -1
        genes=['A','C','G','T']
        queue=deque([(start,0)])
        visited=set([start])

        while queue:
            curr,steps=queue.popleft()
            if curr==end:
                return steps
            for i in range(len(curr)):
                for g in genes:
                    if g!=curr[i]:
                        mutation=curr[:i]+g+curr[i+1:]
                        if mutation in bank_set and mutation not in visited:
                            visited.add(mutation)
                            queue.append((mutation, steps+1))
        return -1