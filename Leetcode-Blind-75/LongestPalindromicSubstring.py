class Solution:
    def longestPalindrome(self,s:str) -> str:
        res=""
        resLen=0

        for i in range(len(s)):
            # odd length
            l,r=i,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r -l +1) > resLen:
                    res=s[l:r+1]
                    resLen= (r-l+1)
                l-=1
                r+=1
            # even length
            l,r= i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if( r- l +1) > resLen:
                    res= s[l:r+1]
                    resLen= (r-l+1)
                l-=1
                r+=1
        return res

my_obj = Solution()
print(my_obj.longestPalindrome("cbbd"))


'''


class Solution:
    def lengthLongestSubstring(self,strs:str)-> str:
        res=""
        resLen=0

        for i in range(len(strs)):
            res,resLen=self.checkPalin(strs,i,i+1,resLen,res)
            res,resLen =self.checkPalin(strs,i,i,resLen,res)

        return res

    def checkPalin(self,strs,l,r,resLen,res):
        while l >= 0 and r < len(s) and strs[l] == strs[r]:
            if (r-l+1) > resLen:
                res=strs[l:r+1]
                resLen= r-l+1
            l-=1
            r+=1
        return res,resLen

myObj= Solution()
s = "ac"
print(myObj.lengthLongestSubstring(s))

'''
