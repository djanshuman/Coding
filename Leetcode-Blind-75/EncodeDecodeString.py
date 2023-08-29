
#https://www.lintcode.com/problem/659/

from typing import List

class Solutions:

    def encode(self, strs:List[str]) -> str:
        res=""

        for i in strs:
            res+= str(len(i))+"#"+i
        return res

    def decode(self,strs:str) -> str:
        i=0
        res=[]

        while i < len(strs):
            j=i
            while strs[j] != '#':
                j += 1
            lenStr = int(strs[i:j])
            res.append(strs[j + 1:j + 1 + lenStr])
            i=j+1+lenStr
        return res

myobj= Solutions()
print(myobj.encode(["hello","bye","scala"]))
print(myobj.decode("5#hello3#bye5#scala41#john"))
