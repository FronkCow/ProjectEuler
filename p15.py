# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
# there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

# start in top left corner
curr_x = 0
curr_y = 2

traversed_list = []
route_list = []

route_list.append((curr_x, curr_y))

finished = False
