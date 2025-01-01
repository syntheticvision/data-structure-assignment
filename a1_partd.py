# copy over your a1_partd.py file here

#    Main Author(s): Ashkan Rahimpour Harris, Babak Ghafourigivi
#    Main Reviewer(s): Shayan Ramezanzadeh
from a1_partc import Queue


def get_overflow_list(grid):
	rows, cols = len(grid), len(grid[0])
	cells = []
# Loop through each cell in the grid
	for row in range(rows):
		for col in range(cols):
			# Assume the cell has 4 neighbors (interior cell)
			num_neighbors = 4 
			# Adjust number of neighbors for top/bottom row cells
			if row == 0 or row == rows - 1: # Top or bottom
				num_neighbors -= 1
			# Adjust number of neighbors for left/right column cells
			if col == 0 or col == cols - 1: # Left or right
				num_neighbors -= 1
			# Check if the cell's absolute value is greater than or equal to its neighbors
			cell_value = abs(grid[row][col])
			if cell_value >= num_neighbors:
				cells.append((row, col))
	# Return the list of overflowing cells, or None if no cells are overflowing
	return cells if cells else None


def overflow(grid, a_queue):
	cells = get_overflow_list(grid) # Get the list of overflowing cells
	# Base case: if no overflowing cells, return 0
	if not cells:
		return 0
	# Base case: stop if all non-zero cells have the same sign
	if all(value < 0 for row in grid for value in row if value) or all(value > 0 for row in grid for value in row if value):
		return 0

	manage_list = []
	# Loop through each overflowing cell
	for row, col in cells:
		 # Store the sign of the cell
		if grid[row][col] > 0: manage_list.append(1)
		else:
			manage_list.append(-1)
		grid[row][col] = 0 
	# Spread the overflow to neighboring cells
	for i, (row, col) in enumerate(cells):
		for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]: # Check neighbors
			x, y = row + dx, col + dy
			# Ensure the neighbor is within grid bounds
			if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
				# Increase the neighbor's value
				grid[x][y] = (abs(grid[x][y]) + 1) * manage_list[i] 
	# Add the updated grid to the queue
	a_queue.enqueue([row[:] for row in grid]) # recursive call for further overflow

	# Recursive call to handle further overflows
	return 1 + overflow(grid, a_queue)  