# BFS CODE PATTERN

# procedure BFS(Graph, root) is
#     let Q be a queue
#     label root as discovered 
#     Q.append(root)

#     while Q is not empty do
#         v = Q.pop()
#         if v is the goal then
#             return v
        
#         for all edges from v to w in G.adjacentEdges(v) do
#             if w is not labeled as discovered then
#                 label w as discovered
#                 Q.append(w)


# Dijkstra Shortest Path Algorithm
# 1. Find adjacent nodes of source node
# 2. Find cost of each neighbouring node, cost(current_node) = cost(parent_node) + distance(parent_node -> current_node)
# 3. Compare the node costs
# 4. Find the minimum cost neighbour
# 5. Mark current_node visited
