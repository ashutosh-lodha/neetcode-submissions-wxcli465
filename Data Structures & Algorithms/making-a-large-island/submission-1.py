class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        n = len(grid)

        island_sizes = {}
        island_id = 2

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Find an entire island using iterative DFS.
        def dfs(row, col, island_id):

            # Use our own stack instead of recursive function calls.
            stack = [(row, col)]

            # Mark the starting cell so we don't visit it again.
            grid[row][col] = island_id

            area = 0

            while stack:

                # Take one cell from the stack.
                current_row, current_col = stack.pop()

                # Count this cell as part of the island.
                area += 1

                # Check all four neighboring cells.
                for dr, dc in directions:

                    new_row = current_row + dr
                    new_col = current_col + dc

                    # Check that the neighbor is inside the grid
                    # and is land that has not been visited.
                    if (0 <= new_row < n and
                        0 <= new_col < n and
                        grid[new_row][new_col] == 1):

                        # Mark it immediately to avoid adding it twice.
                        grid[new_row][new_col] = island_id

                        # Add it to the stack so we can explore it later.
                        stack.append((new_row, new_col))

            return area

        # STEP 1: Find and label all existing islands.
        for row in range(n):
            for col in range(n):

                if grid[row][col] == 1:

                    area = dfs(row, col, island_id)

                    island_sizes[island_id] = area

                    island_id += 1

        # Find the largest island that already exists.
        largest_area = max(island_sizes.values(), default=0)

        # STEP 2: Try changing every zero into one.
        for row in range(n):
            for col in range(n):

                if grid[row][col] == 0:

                    # Store distinct neighboring island IDs.
                    neighboring_islands = set()

                    for dr, dc in directions:

                        new_row = row + dr
                        new_col = col + dc

                        if 0 <= new_row < n and 0 <= new_col < n:

                            if grid[new_row][new_col] > 1:
                                neighboring_islands.add(grid[new_row][new_col])

                    # Start with 1 for the zero we are changing.
                    current_area = 1

                    # Add the area of every distinct neighboring island.
                    for island in neighboring_islands:
                        current_area += island_sizes[island]

                    largest_area = max(largest_area, current_area)

        return largest_area