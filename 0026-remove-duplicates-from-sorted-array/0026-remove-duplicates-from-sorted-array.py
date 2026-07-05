class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # Edge case: If the array is empty, return 0
        if not nums:
            return 0
        
        # 'write_ptr' tracks where the next unique element should be placed
        write_ptr = 1
        
        # 'read_ptr' scans through the array starting from the second element
        for read_ptr in range(1, len(nums)):
            # If the current element is different from the previous one, it is unique
            if nums[read_ptr] != nums[read_ptr - 1]:
                nums[write_ptr] = nums[read_ptr]
                write_ptr += 1
                
        # The position of write_ptr equals the total count of unique elements
        return write_ptr
