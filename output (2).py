def format_steps(steps):
    """Format the steps as a clean, readable string."""
    return " → ".join([f"({x},{y})" for x, y in steps])

def print_path_on_maze(maze, steps):
    """Print the maze with the path represented by '*'."""
    maze_copy = [row[:] for row in maze]  # Make a copy of the maze
    for x, y in steps:
        if maze_copy[x][y] == 0:  # Avoid replacing walls with '*'
            maze_copy[x][y] = "*"
    for row in maze_copy:
        print(" ".join(str(cell) if cell != "*" else "*" for cell in row))
