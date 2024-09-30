class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        # Edge case: If the grid is empty, return 0
        if not grid:
            return 0
        
        # Grid dimensions
        rows, cols = len(grid), len(grid[0])
        
        # Visited array to keep track of visited landmasses
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        
        # Helper function to perform DFS and mark all connected 'L' as visited
        def dfs(r, c):
            # Check for boundaries and whether the cell is unvisited land ('L')
            if r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c] or grid[r][c] == 'W':
                return
            # Mark this cell as visited
            visited[r][c] = True
            # Visit all 4 possible directions (up, down, left, right)
            dfs(r-1, c)  # up
            dfs(r+1, c)  # down
            dfs(r, c-1)  # left
            dfs(r, c+1)  # right
        
        # Count the number of distinct islands
        island_count = 0
        for r in range(rows):
            for c in range(cols):
                # If the current cell is land ('L') and hasn't been visited, it's a new island
                if grid[r][c] == 'L' and not visited[r][c]:
                    # Perform DFS to mark all parts of this island
                    dfs(r, c)
                    # Increment the island count
                    island_count += 1
        
        return island_count