from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Count character frequencies in both strings
        note_counts = Counter(ransomNote)
        magazine_counts = Counter(magazine)
        
        # Check if magazine has enough of each character needed
        for char, count in note_counts.items():
            if magazine_counts[char] < count:
                return False
                
        return True

        