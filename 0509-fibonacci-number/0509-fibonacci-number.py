   
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        n2, n1 = 0, 1
        for _ in range(2, n + 1):
            n2, n1 = n1, n2 + n1
            
        return n1
