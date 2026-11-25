import collections
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dire = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        q = collections.deque()
        res = 0

        def bfs(x, y):
            q.append((x, y))
            grid[x][y] = 1
            is_closed = True
            while q:                
                x, y = q.popleft()

                for dx, dy in dire:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny < 0 or nx >= ROWS or ny >= COLS:
                        is_closed = False
                        continue
                    if grid[nx][ny] == 1:
                        continue
                    grid[nx][ny] = 1
                    q.append((nx, ny))
            return is_closed

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    res += bfs(r, c)
        return res

