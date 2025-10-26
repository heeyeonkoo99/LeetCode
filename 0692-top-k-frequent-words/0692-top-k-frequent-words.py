from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # counter써버리기..?
        count=Counter(words)
        heap=[(-freq,word) for word, freq in count.items()]
        heapq.heapify(heap)
        res=[heapq.heappop(heap)[1] for _ in range(k)]
        return res
        