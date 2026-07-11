class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1] * n
        
        # Pass 1: Calculate prefix products (left to right)
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
            
        # Pass 2: Calculate suffix products and combine (right to left)
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
            
        return answer
