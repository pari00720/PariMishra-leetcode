class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1  # Move s pointer only when characters match
            j += 1      # Always move t pointer
            
        return i == len(s)  # True if all characters of s were found
