"""
Traverse a graph using Depth First Search (DFS).
DFS explores as deep as possible along a branch before backtracking.
"""

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}

def dfs(graph, start):

    visited = []
    stack = [start]

    while stack:

        node = stack.pop()
        
        if node not in visited:
            visited.append(node)
        
            for neighbor in graph[node]:
                stack.append(neighbor)
    
    return visited

print(dfs(graph, "A"))