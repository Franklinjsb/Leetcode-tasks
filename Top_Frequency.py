#Find the Top Frequency in an array

from collections import Counter

nums = [1,2,1,2,1,2,3,1,3,2]

k=2




class Solution(object):
  def topKFrequent(self, nums, k):
      maiores = Counter(nums)
      repetidos=[]
      for valor, freq in maiores.most_common():
          #print(maiores)
          repetidos.append(valor)
          if len(repetidos) == k:
            return repetidos
      
sol = Solution()
print(sol.topKFrequent(nums, k))