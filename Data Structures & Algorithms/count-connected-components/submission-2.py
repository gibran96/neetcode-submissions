class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # DFS solution
        # edgeMap = {i: [] for i in range(n)}

        # for e1, e2 in edges:
        #     edgeMap[e1].append(e2)
        #     edgeMap[e2].append(e1)
        
        # print(edgeMap)
        # visit = [False] * n

        # def dfs(node):
        #     for n in edgeMap[node]:
        #         if not visit[n]:
        #             visit[n] = True
        #             dfs(n)
        
        # res = 0
        # for node in range(n):
        #     if not visit[node]:
        #         visit[node] = True
        #         dfs(node)
        #         res += 1
        # return res

        # Disjoint set union
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = n1
            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            if rank[p2] > rank[p1]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            return 1
        
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res