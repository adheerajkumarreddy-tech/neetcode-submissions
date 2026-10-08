class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        k=target
        while(i<j):
            sum=numbers[i]+numbers[j]
            if(sum==k):
                return [i+1,j+1]
            elif(sum>k):
                j=j-1
            else:
                i=i+1
        
        return 0