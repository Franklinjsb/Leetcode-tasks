#Find the bigger values in an array

nums = [8,1,2,2,3]

class Solution(object):
  def encontrarmaioresmenores(self, nums):
      numsconfere = nums
      contagem = 0
      conferencia = []

      for num in range(len(nums)):
        for i in range( len(numsconfere)) :
          if nums[num]> numsconfere[i]:
            contagem +=1
        conferencia.append(contagem)
        contagem = 0
        
              
              
      
      return conferencia

sol = Solution()
print(sol.encontrarmaioresmenores(nums))