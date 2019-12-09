"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex not found.")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise IndexError("Vertex not found.")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = Queue()
        queue.enqueue(starting_vertex)
        visited = set()
        while queue.size():
            current_vert = queue.dequeue()
            if current_vert not in visited:
                print(f"BFT: {current_vert}")
                visited.add(current_vert)
                for vert in self.get_neighbors(current_vert):
                    queue.enqueue(vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        stack.push(starting_vertex)
        visited = set()
        while stack.size():
            current_vert = stack.pop()
            if current_vert not in visited:                
                print(f"DFT: {current_vert}")
                visited.add(current_vert)
                for vert in self.get_neighbors(current_vert):
                    stack.push(vert)
                
    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        print(f"Recursive DFT: {starting_vertex}")
        visited.add(starting_vertex)
        for vert in self.get_neighbors(starting_vertex):
            if vert not in visited:
                self.dft_recursive(vert, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        visited = set()
        queue = Queue()
        queue.enqueue([starting_vertex])
        while queue.size():
            current_path = queue.dequeue()
            current_vert = current_path[-1]
            if current_vert == destination_vertex:
                return current_path
            if current_vert not in visited:
                visited.add(current_vert)
                for vert in self.get_neighbors(current_vert):
                    queue.enqueue(current_path + [vert])
        return False

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        visited = set()
        stack = Stack()
        stack.push([starting_vertex])
        while stack.size():
            current_path = stack.pop()
            current_vert = current_path[-1]
            if current_vert == destination_vertex:
                return current_path
            if current_vert not in visited:
                visited.add(current_vert)
                for vert in self.get_neighbors(current_vert):
                    stack.push(current_path + [vert])
        return False

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        """
        print(f"Recursive DFT: {starting_vertex}")
        visited.add(starting_vertex)
        for vert in self.get_neighbors(starting_vertex):
            if vert not in visited:
                self.dft_recursive(vert, visited)
        """
        if visited is None:
            visited = set()
        if path is None:
            path = []
        path.append(starting_vertex)
        visited.add(starting_vertex)
        if starting_vertex == destination_vertex:
            return path
        for vert in self.get_neighbors(starting_vertex):
            print(self.get_neighbors(starting_vertex))
            if vert not in visited:
                return self.dfs_recursive(vert, destination_vertex, visited, path)


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)
    breakpoint()
    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1,6))
