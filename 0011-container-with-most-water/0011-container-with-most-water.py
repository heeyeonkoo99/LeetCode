class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 정말 직관적으로 생각했을떄 Brute force로 풀수있지만 시간복잡도가 O(N^2)이다. 따라서 Two pointer로 해야함

        left=0
        right=len(height)-1
        max_area=0
        while (right-left>0):
            max_area=max(max_area,(right-left)*min(height[left],height[right]))
            if height[left]>=height[right]:
                right-=1
            else:
                left+=1
        return max_area





        