class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h_index=0
        citations.sort(reverse=True)

        for i,v in enumerate(citations):
            if v>=i+1:
                h_index=i+1 
            else:
                break
        return h_index

        