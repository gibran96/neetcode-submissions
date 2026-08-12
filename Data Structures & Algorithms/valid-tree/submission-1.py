class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        treeMap = {i: [] for i in range(n)}

        for edge in edges:
            treeMap[edge[0]].append(edge[1])
            treeMap[edge[1]].append(edge[0])
        
        print(treeMap)

        visitSet = set()

        def dfs(node, prev):
            if node in visitSet:
                return False
            visitSet.add(node)
            for n in treeMap[node]:
                if n == prev: continue
                if not dfs(n, node): return False
            return True
        
        return dfs(0, -1) and n == len(visitSet)
