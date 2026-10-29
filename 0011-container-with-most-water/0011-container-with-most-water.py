class Solution:
    def maxArea(self, height: list[int]) -> int:
    
        maximum=0
        left,right=0,len(height)-1
        while left<right:
            temp=(right-left+1)*min(height[left],height[right])
            if height[left]<height[right]:
                right-=1
            else:
                left+=1

            maximum=max(maximum,temp)

        return maximum
        