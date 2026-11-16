import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)

        for a, b in prerequisites:
            adj[a].append(b)
        
        visit = set()

        def dfs(i):
            if i in visit:
                return False
            if adj[i] == []:
                return True
            
            visit.add(i)
            for c in adj[i]:
                if not dfs(c):
                    return False
            visit.remove(i)
            adj[i] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
