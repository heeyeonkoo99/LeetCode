class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:

        start=0
        total=0
        current=0
        for i in range(len(gas)):
            diff=gas[i]-cost[i]
            total+=diff
            current+=diff
            if current<0:
                start=i+1
                current=0
        return start if total>0 else -1