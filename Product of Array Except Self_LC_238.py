class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        leftProduct = 1
        for i in range(len(nums)):
            result.append(leftProduct)
            leftProduct = leftProduct * nums[i]
      
        rightProduct = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] = result[i] * rightProduct
            rightProduct = rightProduct * nums[i] 
        return result
            

           
