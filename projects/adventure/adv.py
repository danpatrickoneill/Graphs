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

def explore():
    my_path = []
    rooms = {}
    previous_room = None
    previous_move = None
    count = 0
    travel_path = deque()
    while len(rooms) < len(roomGraph):
    # while count < 10:
        current_room = player.currentRoom
        current_exits = current_room.getExits()
        # print(f"Current room: {current_room.id} with exits to: {current_exits}")
        if current_room.id not in rooms:
            rooms[current_room.id] = {e: '?' for e in current_exits}
            # print(f"Rooms with new room just added: {rooms}")
        unexplored = [e for e in current_exits if rooms[current_room.id][e] == '?']
        # print(f"Unexplored: {unexplored}")
        if len(travel_path):
            next_move = travel_path.popleft()
        elif len(unexplored):
            # if previous_move in unexplored:
            #     next_move = previous_move
            # else:
            next_move = random.choice(unexplored)
        else:
            # try:
            #     next_move = random.choice([e for e in current_exits if rooms[current_room.id][e] != previous_room.id])
            # except:
            #     next_move = opposite_directions[next_move]
            travel_path = find_new_path(rooms, current_room)
            next_move = travel_path.popleft()
        # if previous_move:
        #     print(previous_move in rooms[current_room.id] and rooms[current_room.id][previous_move] == '?')
        #     if previous_move in rooms[current_room.id] and rooms[current_room.id][previous_move] == '?':
        #         print(previous_move, next_move, rooms[current_room.id])
        #         next_move = previous_move

        previous_room = current_room
        traversalPath.append(next_move)
        my_path.append(next_move)
        player.travel(next_move)
        # previous_move = next_move
        # print(f"Next move: {next_move}")
        current_room = player.currentRoom
        # print(f"Moved from room {previous_room.id} to room {current_room.id}")
        if current_room.id not in rooms:
            current_exits = current_room.getExits()
            rooms[current_room.id] = {e: '?' for e in current_exits}
            # print(f"Rooms with new room just added: {rooms}")
        rooms[previous_room.id][next_move] = current_room.id
        # print(previous_room.id, current_room.id)
        rooms[current_room.id][opposite_directions[next_move]] = previous_room.id
        # print("Connecting back, ",current_room.id, opposite_directions[next_move], previous_room.id)
        # if len(rooms) % 50 == 0:
        #     print(f"Rooms so far: {rooms}")
        # print(f"Traversal path: {traversalPath}")
        # count += 1
    # print(rooms)
    return my_path

    


# TRAVERSAL TEST
# My function that sets up traversal path
explore()

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

tries = 100000
moves_list = []
for _ in range(tries):
    # TRAVERSAL TEST
    # My function that sets up traversal path
    player = Player("Name", world.startingRoom)
    traversalPath = []
    explore()

    visited_rooms = set()
    player.currentRoom = world.startingRoom
    visited_rooms.add(player.currentRoom.id)


    # print(traversalPath)
    # print(len(traversalPath))

    for move in traversalPath:
        player.travel(move)
        visited_rooms.add(player.currentRoom.id)

    # print(visited_rooms)
    if len(visited_rooms) == len(roomGraph):
        moves_list.append(traversalPath)
        # print(f"TESTS PASSED: {len(traversalPath)} moves, {len(visited_rooms)} rooms visited")
    else:
        print("TESTS FAILED: INCOMPLETE TRAVERSAL")
        print(f"{len(roomGraph) - len(visited_rooms)} unvisited rooms")

moves_dict = {len(path): path for path in moves_list}
length_list = [len(path) for path in moves_list]
print(len(moves_list), "runs:")
print(f"Shortest path: {moves_dict[min(length_list)]}")
print(f"Minimum: {min(length_list)}, Maximum: {max(length_list)}")
print("Average: ", sum(length_list) / tries)

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
