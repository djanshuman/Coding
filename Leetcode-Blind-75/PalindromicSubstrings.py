class Solution:
  def countSubstrings(self, s:str) -> int:

      res=0
      l=0
      r=0

      for i in range(len(s)):
          res+= self.palin(s,i,i)
          res += self.palin(s, i, i+1)
      return res

  def palin(self,s,l,r):
      res=0
      while l >= 0 and r < len(s) and s[l] == s[r]:
          res+=1
          l-=1
          r+=1
      return res

my_obj = Solution()
print(my_obj.countSubstrings("aaa"))

'''

class Solution:
    def lengthLongestSubstring(self,s:str)-> int:
        count=0

        for i in range(len(s)):
            count=self.checkPalin(s,i,i+1,count)
            count=self.checkPalin(s,i,i,count)

        return count

    def checkPalin(self,s,l,r,count):
        while l >= 0 and r < len(s) and s[l] == s[r]:
                count+=1
                l-=1
                r+=1
        return count

myObj= Solution()
s = "aaa"
print(myObj.lengthLongestSubstring(s))

'''
