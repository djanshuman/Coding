class Solution:
    def isValid(self, s: str) -> bool:
        pair = {']':'[','}':'{',')':'('}
        curr = []
        for i in s:
            if i in pair:
                if (len(curr) == 0 or curr.pop() != pair[i]):
                    return False
            else:
                curr.append(i)

        if len(curr) != 0:
            return False
        return True

new_obj= Solution()
print(new_obj.isValid("({[]})"))
