class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        bank_set=set(bank)
        visited=set([startGene])
        queue=deque([(startGene,0)])
        gene=["A","C","G","T"]
        if endGene not in bank_set:
            return -1
        while queue:
            curr,steps=queue.popleft()
            if curr==endGene:
                    return steps
            for i in range(len(curr)):
                
                for g in gene:
                    if g!=curr[i]:
                        temp=curr[:i]+g+curr[i+1:]
                        if temp in bank_set and temp not in visited:
                            visited.add(temp)
                            queue.append((temp,steps+1))
        return -1


        