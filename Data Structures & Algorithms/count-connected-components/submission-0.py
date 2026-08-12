class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        edgeMap = {i: [] for i in range(n)}

        for e1, e2 in edges:
            edgeMap[e1].append(e2)
            edgeMap[e2].append(e1)
        
        print(edgeMap)
        visit = [False] * n

        def dfs(node):
            for n in edgeMap[node]:
                if not visit[n]:
                    visit[n] = True
                    dfs(n)
        
        res = 0
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                res += 1
        return res