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


# tries = 10000
# moves_list = []
# for _ in range(tries):
#     # TRAVERSAL TEST
#     # My function that sets up traversal path
#     player = Player("Name", world.startingRoom)
#     traversalPath = []
#     explore()

#     visited_rooms = set()
#     player.currentRoom = world.startingRoom
#     visited_rooms.add(player.currentRoom.id)


#     # print(traversalPath)
#     # print(len(traversalPath))

#     for move in traversalPath:
#         player.travel(move)
#         visited_rooms.add(player.currentRoom.id)

#     # print(visited_rooms)
#     if len(visited_rooms) == len(roomGraph):
#         moves_list.append(traversalPath)
#         # print(f"TESTS PASSED: {len(traversalPath)} moves, {len(visited_rooms)} rooms visited")
#     else:
#         print("TESTS FAILED: INCOMPLETE TRAVERSAL")
#         print(f"{len(roomGraph) - len(visited_rooms)} unvisited rooms")

# moves_dict = {len(path): path for path in moves_list}
# length_list = [len(path) for path in moves_list]
# print(len(moves_list), "runs:")
# print(f"Shortest path: {moves_dict[min(length_list)]}")
# print(f"Minimum: {min(length_list)}, Maximum: {max(length_list)}")
# print("Average: ", sum(length_list) / tries)


#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
