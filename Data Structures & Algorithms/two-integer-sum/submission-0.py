class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d={}

        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in d:
                val,ind=d[diff]
                return [ind,i]
            else:
                d[nums[i]]=[diff,i]

        return [0,0]