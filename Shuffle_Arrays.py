#Shuffle values in an array from a variable.
nums = [1,1,2,2]
n = 2


class Solution(object):
  def shuffle(self, nums, n):
    nums2 = []
    for i in range(n):
      nums2.append(nums[i])
      nums2.append(nums[i+n])
    return nums2

sol= Solution()
print(sol.shuffle(nums, n))
