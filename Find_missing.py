#Find missing in an array
nums = [1,1]

class Solution(object):
  def encontrarfaltando(self, nums):
    corrigido=[]
    nums.sort()
    maior = set(nums)
   
  
    
    for num in range(1, len(nums)+1):
      if num not in maior:
        corrigido.append(num)
    return corrigido

sol = Solution()
print(sol.encontrarfaltando(nums))