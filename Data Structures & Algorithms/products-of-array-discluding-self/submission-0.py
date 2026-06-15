class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lp=self.leftProduct(nums)
        rp=self.leftProduct(nums[::-1])
        rp=rp[::-1]
        f=[]
        for i in range(len(nums)):
            f.append(lp[i]*rp[i])



        return f

    def leftProduct(self,a):
        lp=[1]
        l=1
        for i in range(len(a)-1):
            l=a[i]*l
            lp.append(l)

        return lp