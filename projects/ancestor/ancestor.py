from graph import Graph
from util import Stack, Queue

def earliest_ancestor(ancestors, starting_node):
    tree = Graph()
    for pair in ancestors:
        parent, child = pair[0], pair[1]
        tree.add_vertex(parent)
        tree.add_vertex(child)
        tree.add_edge(child, parent)
    # if not tree.get_neighbors(starting_node):
    #     return -1
    path = []
    queue = Queue()
    queue.enqueue(starting_node)
    visited = set()
    while queue.size():
        node = queue.dequeue()
        if node not in visited:
            visited.add(node)
            path.append(node)
            for n in tree.get_neighbors(node):
                queue.enqueue(n)
    if len(path) == 1:
        return -1
    print(starting_node, path)
    return path[-1]

# Recursive, non-graph solution
# parents = [t for t in ancestors if t[1] == starting_node]
# if len(parents) == 0:
#     if child:
#         return -1
#     return starting_node
# for p in parents:
#     return earliest_ancestor(ancestors, p[0], False)

if __name__ == "__main__":
        
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    # print(earliest_ancestor(test_ancestors, 1))
    # print(earliest_ancestor(test_ancestors, 2))
    print(earliest_ancestor(test_ancestors, 3))
    # print(earliest_ancestor(test_ancestors, 4))
    # print(earliest_ancestor(test_ancestors, 5))
    # print(earliest_ancestor(test_ancestors, 6))
    # print(earliest_ancestor(test_ancestors, 7))
    # print(earliest_ancestor(test_ancestors, 8))
    # print(earliest_ancestor(test_ancestors, 9))
    # print(earliest_ancestor(test_ancestors, 10))
    # print(earliest_ancestor(test_ancestors, 11))