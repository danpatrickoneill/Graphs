from collections import deque  # These may come in handy

'''
Write a function that takes a 2D binary array and returns the number of 1 islands.
An island consists of 1s that are connected to the north, south, east or west.

For example:
'''

# 1. Translate the problem into graphs terminology you've learned this week
# 2. Build your graph
# 3. Traverse your graph


def island_counter(matrix):
    ### we’re probably going to loop through the islands,
    ### do bfs on them and count how many times that BFT occurs\
    pass

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

print(island_counter(islands)) # returns 4

# islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
#            [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
#            [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
#            [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
#            [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
#            [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
#            [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
#            [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
#            [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
#            [0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
#            [1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
#            [1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
#            [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]]

# print(island_counter(islands))  # 14


