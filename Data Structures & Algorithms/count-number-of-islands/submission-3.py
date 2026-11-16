class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        drc = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # def dfs(r, c):
        #     if (min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == '0'):
        #         return
        #     grid[r][c] = '0'

        #     dfs(r + 1, c)
        #     dfs(r - 1, c)
        #     dfs(r, c + 1)
        #     dfs(r, c - 1)

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = '0'

            while q:
                row, col = q.popleft()
                for dr, dc in drc:
                    if (min(row + dr, col + dc) < 0 or 
                        row + dr >= ROWS or 
                        col + dc >= COLS or 
                        grid[row + dr][col + dc] == '0'):
                        continue
                    grid[row + dr][col + dc] = '0'
                    q.append((row + dr, col + dc))
                    

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':        
                    # dfs(r, c)
                    bfs(r, c)
                    islands += 1

        return islands
            