#Count binary in sequency

nums=[1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1]

class Solution(object):
  def encontraconsecutivos(self, nums):
    countconsecutivos = 0
    maxconsecutivos = 0
    n = len(nums)

    for i in range(n):
      if nums[i] == 1:
        countconsecutivos +=1
        maxconsecutivos = max(maxconsecutivos, countconsecutivos)

      else:
        conuntconsecutivos = 0


    return maxconsecutivos



sol = Solution()
print(sol.encontraconsecutivos(nums))