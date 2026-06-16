class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        barr=[]


        if len(nums)==0:
            return 0
        se=set(nums)

        for val in nums:
            if val-1 not in se:
                barr.append(val)
        
        maxi=max(nums)
        carr=[]
        for b in barr:
            c=1
            x=b
            while((x+1 in se) and x+1<= maxi):
                c+=1
                x=x+1
            carr.append(c)

        return max(carr)