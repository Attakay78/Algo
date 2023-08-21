from collections import deque

class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.data = {}
        self.paths = []

        for edge1, edge2 in self.edges:
            if edge1 in self.data:
                self.data[edge1].append(edge2)
            else:
                self.data[edge1] = [edge2]
    
    def get_paths(self, start, end, path=[]):
        if start not in self.data:
            return []
        
        path = path + [start]

        if start == end:
            self.paths.append(path)

        for node in self.data[start]:
            if node not in path:
                self.get_paths(node, end, path)
    
    def get_new_paths(self, start, end, path):
        pass

    # find the shortest path
    def get_shortest_path(self, start, end):
        queue = deque()
        queue.append(start)
        visited_nodes = set()
        visited_nodes.add(start)
        parents = {start:start}

        while len(queue) != 0:
            visited_node = queue.popleft()

            # process node
            for node in self.data.get(visited_node, []):
                if node not in visited_nodes:
                    visited_nodes.add(node)
                    queue.append(node)
                    parents[node] = visited_node

        path = []
        current_node = end
        
        while current_node != start:
            path.append(current_node)
            current_node = parents[current_node]

        path.append(current_node)
        return path[::-1]
    
    # BFS implementation
    def bfs(self, start):
        queue = deque()
        visited_nodes = [start]
        queue.append(start)
        distance = {start: 0} #The level distance of all nodes from the root(start)

        while len(queue) != 0:
            visited_node = queue.popleft()

            for node in self.data.get(visited_node, []):
                if node not in visited_nodes:
                    distance[node] = distance[visited_node] + 1
                    queue.append(node)
                    visited_nodes.append(node)
        
        return visited_nodes, distance
    
    # DFS implementation (without recursion, using stack)
    def dfs(self, start):
        stack = deque() #using a queue as a stack
        stack.append(start)
        visited_nodes = []

        while len(stack) != 0:
            current_node = stack.pop()

            if current_node not in visited_nodes:
                visited_nodes.append(current_node)
                for node in self.data.get(current_node, []):
                    if node not in visited_nodes:
                        stack.append(node)
        
        return visited_nodes

    def __repr__(self):
        graph_rep = []
        for key, value in self.data.items():
            graph_rep.append(f"{key} -> {value}")
        
        return "\n".join(graph_rep)
    
    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto")
    ]

    routes_2 = [
        (0, 1),
        (0, 3),
        (1, 2),
        (2, 3),
        (4, 5),
        (4, 6),
        (5, 6),
        (7, 8)
    ]

    graph = Graph(edges=routes)
    print(graph)

    graph.get_paths("Mumbai", "New York")
    # print(graph.paths)
    print(graph.get_shortest_path("Mumbai", "New York"))

    print(graph.bfs("Mumbai"))
    print(graph.dfs("Mumbai"))

    # graph_2 = Graph(edges=routes_2)
    # print(graph_2)

    # graph_2.get_paths(0, 3)
    # print(graph_2.paths)
    # # print(graph_2.get_shortest_path(0, 3))
    # print(graph_2.bfs(4))
