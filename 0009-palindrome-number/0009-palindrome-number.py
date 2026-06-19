
class Solution:
    def isPalindrome(self, x: int) -> bool:
    
        if x < 0:
            return False
            
        org_num = x
        reversed_num = 0
        
        while x > 0:
            n = x % 10
            reversed_num = (reversed_num * 10) + n
            x = x // 10
            
        
        return org_num == reversed_num
