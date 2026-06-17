#Code to concatenate two different arrays

#inputs
nums2 = [1,2,3,1]
nums = [1,2,3,1]

#main function execution using for looping
def function(nums):

    n = len(nums)

    ans = [0] *(2*n)


    for i in range(n):
      
      ans[i] = nums[i]

      ans[i+n] = nums[i]

    return ans

print(function(nums))

#Recursive function model

def function_recursive(nums2):
  return nums2 + nums2

print(function_recursive(nums2))