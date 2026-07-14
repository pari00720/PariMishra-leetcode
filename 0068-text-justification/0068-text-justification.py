
class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res = []
        current_line = []
        current_length = 0  # Total characters of words in current_line (excluding spaces)
        
        for word in words:
            # Check if adding the next word (plus a minimum 1 space gap) exceeds maxWidth
            if current_length + len(word) + len(current_line) > maxWidth:
                # Justify the current line before moving to the next
                res.append(self._justify_line(current_line, current_length, maxWidth))
                current_line = []
                current_length = 0
                
            current_line.append(word)
            current_length += len(word)
            
        # Handle the last line (must be left-justified)
        last_line_str = " ".join(current_line)
        trailing_spaces = maxWidth - len(last_line_str)
        res.append(last_line_str + " " * trailing_spaces)
        
        return res
        
    def _justify_line(self, line: list[str], current_length: int, maxWidth: int) -> str:
        # Case 1: Line contains only 1 word, must be left-justified
        if len(line) == 1:
            return line[0] + " " * (maxWidth - current_length)
            
        # Case 2: Multi-word line, fully justify by distributing spaces evenly
        total_spaces = maxWidth - current_length
        gaps = len(line) - 1
        
        base_spaces = total_spaces // gaps
        extra_spaces = total_spaces % gaps
        
        # Reconstruct the line string with appropriate spaces between words
        res_str = ""
        for i in range(gaps):
            res_str += line[i]
            # Add base spaces + 1 extra space to the leftmost gaps if there's a remainder
            res_str += " " * (base_spaces + (1 if i < extra_spaces else 0))
            
        res_str += line[-1]  # Append the last word
        return res_str
        