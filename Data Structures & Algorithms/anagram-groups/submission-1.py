class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashMap={}
        for word in strs:
            tup = self.createTuple(word)
            if (tup in hashMap):
                hashMap[tup].append(word)
            else:
                hashMap[tup]=[word]
        ans=[]
        for val in hashMap.values():
            ans.append(val)
        print(hashMap)
        print(ans)
        return ans
    def createTuple(self,word):
        lis=[0]*26;
        for ch in word:
            lis[ord(ch)-ord('a')]+=1
        return tuple(lis)