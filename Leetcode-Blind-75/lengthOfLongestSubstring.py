class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest , start = 0,0
        used ={}

        for i , char in enumerate(s):
            if char in used and used[char] >= start:
                start= used[char] +1
                used[char] = i
            else:
                used[char]=i
                if longest < i - start +1:
                    longest= i - start +1
        return longest

new_obj= Solution()
print(new_obj.lengthOfLongestSubstring("pwwkew"))


'''
pwwkew

p 0
w 1 
w 2
k 3
e 4
w 5

longest 2
start 2
used -> p 0 
        w 2
        k 3 
  
'''
