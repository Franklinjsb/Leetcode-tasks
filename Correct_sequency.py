#Find the number duplicate and change for the correct in the sequency


nums = [1,2,2,4]



class Solution(object):
  def corrigirsequência(self, nums):
    corrigido=[]
    nums.sort()
    maior = set(nums)
   
  
    for i in range(1, len(nums)):
      if nums[i-1]== nums[i]:
        corrigido.append(nums[i])
    for num in range(1, len(nums)+1):
      if num not in maior:
        corrigido.append(num)
    return corrigido

sol = Solution()
print(sol.corrigirsequência(nums))