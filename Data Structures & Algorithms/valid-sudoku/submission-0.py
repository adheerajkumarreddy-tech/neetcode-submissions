class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        self.validrow(board)
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                if(self.validbox(board,i,j)==False):
                    return False
        return self.validrow(board)
        

    def validbox(self,arr,x,y):
        ans=[]
        s=set()
        for i in range(3):
            for j in range(3):
                if(arr[x+i][y+j]=='.'):
                    continue
                ele=arr[x+i][y+j]
                s.add(ele)
                ans.append(ele)

       
        if len(ans)!=len(s):
            return False
        return True
        

    def validrow(self,arr):
        rd={}
        cd={}
        for i in range(9):
            rd[i]=[]
            cd[i]=[]
        for i in range(0,9):
            for j in range(0,9):
                if arr[i][j]=='.':
                    continue
                else:
                    ele=arr[i][j]
                    rd[i].append(ele)
                    cd[j].append(ele)
        for key in rd:
            if(len(set(rd[key]))!=len(rd[key])):
                return False
        for key in cd:
            if(len(set(cd[key]))!=len(cd[key])):
                return False
        return True
    

        
