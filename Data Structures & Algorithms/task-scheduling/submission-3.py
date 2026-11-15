class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for t in tasks:
            count[t] = 1 + count.get(t, 0)
        
        maxF = max(count.values())
        maxCount = 0
        for t, c in count.items():
            maxCount += 1 if c == maxF else 0
        
        res = (maxF - 1) * (n + 1) + maxCount
        return max(len(tasks), res)