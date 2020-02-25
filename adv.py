from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []





# Notes on how to tackle:

# Make a helper fucntion to keep track of the origin/direction of when a player arrives in a new room; north = south; east = west; etc.
def starting_point(direction):

    opposite = {"n": "s", "e": "w", "s": "n", "w": "e"}
    return opposite[direction]

# - use recursive based on lecutre notes and that it will search all instances
# -since we are just traversing the graph we can use an algo similair to bft or dft


 
# -keep track of rooms you've visited, and maintain a path record in a list to return as the final answer
# Track rooms that im visiting
# Track the paths and where im going each time
 # This will be what im returning as the answer 

def depth_recursive_initializer(current_room):
 # just a initalizer to set these variables for the alogrithim
    visited = set()
    path = []


    def depth_recursion(current_room, previous_direction=None):
       
        # when we visit a room/node, we add it to our visited set of rooms just like in the lecture projects
        visited.add(current_room.id)
        # find our options on where we can go by using utility .get_exits method from room.py file
        for exit in current_room.get_exits():
            next_room = current_room.get_room_in_direction(exit)
            # if the exit leads to a (node) room we already visited, then keep trecking on
            if next_room.id in visited:
                continue
            # if the exit leads to a room we havent traversed, then add it to our visited list and to our path as well 
            else:
                visited.add(next_room.id)
                path.append(exit)
            # Run this until all rooms have been visited via recursion;
            depth_recursion(
                current_room.get_room_in_direction(exit),
                previous_direction=exit)
        # This keeps track of our path using the helper function starting_point 
        if previous_direction is not None:
            origin = starting_point(previous_direction)
            path.append(origin)
    # Finaly, Call the function and return the path
    depth_recursion(current_room)
    return path

traversal_path = depth_recursive_initializer(world.starting_room)


#998 moves



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


# Lecture notes used to refactor and devise an algorithim

    # def dfs_recursive(self, starting_vertex, target_value, visited=None, path=None):
   
    # if visited is None:               
    #     visited = set()
    # if path is None:
    #     path = []
    # visited.add(starting_vertex)    # base case 
    # path = path + [starting_vertex] 
    # if starting_vertex == target_value:
    #     return path

    # for child_vertices in self.vertices[starting_vertex]:
    #     if child_vertices not in visited:
    #         new_path = self.dfs_recursive(child_vertices, target_value, visited, path) # recursive action 
    #         if new_path:
    #             return new_path
    # return None  # handles if the target doesn't exist.

    # Recursive functions form lecture notes for refrence:
    # def dft_recursive(self, starting_vertex, visited=None):
  
    #     if visited is None:               
    #         visited = set()
    #     visited.add(starting_vertex)    # base case 
    #     print(starting_vertex)

    #     for child_vertices in self.vertices[starting_vertex]:
    #         if child_vertices not in visited:
    #             self.dft_recursive(child_vertices, visited)  # recursive action 


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")