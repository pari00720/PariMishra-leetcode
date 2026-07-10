class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        # Data Structure: Fixed-size List (Bucket Array)
        buckets = [0] * (n + 1)
        
        # Populate the frequency buckets
        for c in citations:
            if c >= n:
                buckets[n] += 1
            else:
                buckets[c] += 1
                
        # Accumulate papers from highest possible H-index to lowest
        total_papers = 0
        for h in range(n, -1, -1):
            total_papers += buckets[h]
            # If we found at least 'h' papers with >= 'h' citations
            if total_papers >= h:
                return h
                
        return 0
