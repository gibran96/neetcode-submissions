class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS, COLS = len(grid1), len(grid1[0])
        visit = set()
        count = 0
        dire = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visit.add((r, c))
            res = True
            while q:
                tr, tc = q.popleft()
                if grid1[tr][tc] == 0:
                    res = False
                for dr, dc in dire:
                    nr, nc = tr + dr, tc + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and
                        (nr, nc) not in visit and grid2[nr][nc] == 1):
                        visit.add((nr, nc))
                        q.append((nr, nc))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] == 1 and (r, c) not in visit and bfs(r, c):
                    count += 1

        return count