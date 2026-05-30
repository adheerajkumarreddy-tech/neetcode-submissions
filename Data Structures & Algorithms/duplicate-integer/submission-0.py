class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap={}
        for number in nums:
            hashMap[number]=1
        

        return len(nums)!=len(hashMap)
        