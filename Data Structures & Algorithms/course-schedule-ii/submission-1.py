class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        adj = {i: [] for i in range(numCourses)}
        for p in prerequisites:
            c1, c2 = p
            adj[c1].append(c2)

        print(adj)
        visit = set()
        completed = set()

        def dfs(crs):
            if crs in visit:
                return False
            if crs in completed:
                return True
            visit.add(crs)
            for c in adj[crs]:
                if not dfs(c):
                    return False
            completed.add(crs)
            res.append(crs)
            visit.remove(crs)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return res