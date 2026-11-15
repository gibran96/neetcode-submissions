import collections

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        b_len = len(bombs)
        for i in range(b_len):
            for j in range(i + 1, b_len):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]

                d = (x1 - x2)**2 + (y1 - y2)**2

                if d <= r1**2:
                    adj[i].append(j)
                if d <= r2**2:
                    adj[j].append(i)
        
        def dfs(i, visit):
            if i in visit:
                return
            visit.add(i)
            for n in adj[i]:
                dfs(n, visit)
            return len(visit)
        
        res = 0
        for i in range(b_len):
            res = max(res, dfs(i, set()))

        return res 