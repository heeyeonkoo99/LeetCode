class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_sum=0
        current_sum=0
        start=0

        for i in range(len(gas)):
            diff=gas[i]-cost[i]
            total_sum+=diff
            current_sum+=diff
            if current_sum<0:
                start=i+1
                current_sum=0
        return start if total_sum>=0 else -1