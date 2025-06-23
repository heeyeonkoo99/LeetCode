class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i=0
        j=0
        result=[]
        
        while i<m and j<n:
            if nums1[i]<nums2[j]:
                result.append(nums1[i])
                i+=1
            else:
                result.append(nums2[j])
                j+=1
        result.extend(nums1[i:m])
        result.extend(nums2[j:n])

        for k in range(m+n):
            nums1[k]=result[k]
        
        