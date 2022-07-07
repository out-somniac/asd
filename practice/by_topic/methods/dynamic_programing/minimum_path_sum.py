# Given a grid, find a path from the top-left to the bottom-right corner 
# that minimizes the sum of numbers along the path.
# You can only move right or down

def f(grid, F, x, y): # minimum sum that we can get at (x, y)
    if x == 0 and y == 0:
        F[0][0] = grid[0][0]
        return grid[0][0]
    
    if x < 0 or y < 0:
        return float('inf')

    if F[x][y] != -1:
        return F[x][y]
    result = grid[x][y] + min(f(grid, F, x-1, y),
                 f(grid, F, x, y-1))

    F[x][y] = result
    return result    

def min_path_sum(grid):
    F = [[ -1 for i in range(len(grid[0]))] for j in range(len(grid))] 
    return f(grid, F, len(grid) - 1, len(grid[0]) - 1)

if __name__ == "__main__":
    grid = [
        [3, 2, 1, 3],
        [1, 9, 2, 3],
        [9, 1, 5, 4]
    ] # Best path is R, R, D, R, D (R - right, D - down)
    
    print(min_path_sum(grid))