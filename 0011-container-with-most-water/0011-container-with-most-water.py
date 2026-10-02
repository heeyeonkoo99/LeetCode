class Solution:
    def maxArea(self, height: List[int]) -> int:
      
      ans=0
      left,right=0,len(height)-1
      temp=0
      while left<right:
        temp=min(height[left],height[right])*(right-left)
        if height[left]<height[right]:
            left+=1
        else:
            right-=1
        ans=max(ans,temp)
      return ans