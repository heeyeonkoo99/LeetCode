
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d=defaultdict(list)
        for i,v in enumerate(s):
            d[v].append(i)
        ans=[idx[0] for idx in d.values() if len(idx)==1]

        return min(ans) if ans else -1