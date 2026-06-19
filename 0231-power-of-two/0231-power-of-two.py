class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        else:
            ans =1
            range= pow(2,30)
            while(ans<n and n<=range):
               ans = ans*2
        return ans == n         