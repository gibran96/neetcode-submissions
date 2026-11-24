class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # Use symmetry
        x, y = abs(x), abs(y)

        # Ensure x >= y
        if x < y:
            x, y = y, x

        # Handle special cases
        if x == 1 and y == 0:
            return 3

        if x == 2 and y == 2:
            return 4

        # Calculate lower bound
        moves = max(
            (x + 1) // 2,
            (x + y + 2) // 3
        )

        # Adjust parity
        if moves % 2 != (x + y) % 2:
            moves += 1

        return moves