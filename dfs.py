# DFS CODE PATTERN

# procedure DFS_iterative(G, v) is
#     let S be a stack
#     S.push(v)

#     while S is not empty do
#         v = S.pop()

#         if v is not labeled as discovered then
#             label v as discovered
#             for all edges from v to w in G.adjacentEdges(v) do
#                 S.push(w)
