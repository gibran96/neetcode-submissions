class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        memo = {}

        def dfs(x, y):
            if (x, y) in memo:
                return memo[(x, y)]

            if x == 0 and y == 0:
                return 0
            elif x + y == 2:
                return 2
            else:
                memo[(x, y)] = min(dfs(abs(x - 2), abs(y - 1)), dfs(abs(x - 1), abs(y - 2))) + 1
            return memo[(x, y)]
        return dfs(abs(x), abs(y))
