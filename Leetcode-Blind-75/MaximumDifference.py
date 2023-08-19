class Solution:
  def maximumDifference(self, nums: list) -> int:
    ans = -1
    mini = nums[0]

    for i in range(len(nums)):
      if nums[i] > mini:
        ans = max(ans, nums[i] - mini)
      mini = min(mini, nums[i])

    return ans

my_obj = Solution()
print(my_obj.maximumDifference([1,2,5,7,8]))
