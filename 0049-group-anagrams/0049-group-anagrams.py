from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Map sorted strings to their original anagram variations
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Sort the characters of the string to create a uniform key
            # Strings are immutable, so we join the sorted list into a string or tuple
            sorted_key = "".join(sorted(s))
            
            # Append the original string to its corresponding anagram group
            anagram_map[sorted_key].append(s)
            
        # Return all clustered anagram groups as a list of lists
        return list(anagram_map.values())
