from collections import defaultdict
from typing import List

class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      res= defaultdict(list)

      for c in strs:
          count= [0] * 26
          for j in c:
              count[ord(j) - ord("a")] +=1

          res[tuple(count)].append(c)
      return res.values()

my_obj = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(my_obj.groupAnagrams(strs))
