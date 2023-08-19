class Solution:
  def countSubstrings(self, s:str,t:str) -> bool:

      '''

      # O(1) approach
      return sorted(s) == sorted(t)
      '''

      if len(t) != len(s):
          return False

      countS,countT= {},{}

      for i in range(len(s)):
          countS[s[i]]= 1 + countS.get(s[i],0)
          countT[t[i]] = 1 + countT.get(t[i], 0)

      for c in countS:
          if countS[c] != countT.get(c,0):
              return False
      return True


my_obj = Solution()
print(my_obj.countSubstrings("anagram","nagaram"))
