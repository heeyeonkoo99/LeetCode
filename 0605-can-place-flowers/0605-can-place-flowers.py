class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        
        cnt=0
        for i in range(len(flowerbed)):
            if flowerbed[i]==0:
                left_empty=(i==0 or flowerbed[i-1]==0)
                right_empty= (i==len(flowerbed)-1 or flowerbed[i+1]==0)

                if left_empty and right_empty:
                    cnt+=1
                    flowerbed[i]=1

        return cnt>=n
                