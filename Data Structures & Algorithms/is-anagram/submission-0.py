class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        
        a={}
        b={}
        for ch in s:
            if ch in a:
                a[ch]+=1
            else:
                a[ch]=1
        
        for ch in t:
            if ch in b:
                b[ch]+=1
            else:
                b[ch]=1
        
        if a != b:
            return False



        return True

        