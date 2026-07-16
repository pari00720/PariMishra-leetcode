class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                return [left + 1, right + 1] # Convert to 1-indexed
            elif current_sum < target:
                left += 1 # Move left pointer right to increase sum
            else:
                right -= 1 # Move right pointer left to decrease sum
