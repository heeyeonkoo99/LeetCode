class Solution:
    def hIndex(self, citations: List[int]) -> int:

        citations.sort(reverse=True)
        for i,v in enumerate(citations):
            if v>=i:
                return i+1