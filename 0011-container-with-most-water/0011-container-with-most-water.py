class Solution:
    def maxArea(self, height: list[int]) -> int:
    
        maximum=0
        left,right=0,len(height)-1
        while left<right:
            temp=(right-left)*min(height[left],height[right])
            if height[left]<height[right]:
                left+=1
            else:
                right-=1

            maximum=max(maximum,temp)

        return maximum
        