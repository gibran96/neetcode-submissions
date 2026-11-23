import collections
class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # visit = set()
        res = 0

        def bfs(r, c):
            q = collections.deque([(r, c)])
            grid[r][c] = 1
            is_closed = True

            while q:
                x, y = q.popleft()
                for dx, dy in directions:
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