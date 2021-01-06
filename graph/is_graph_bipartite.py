def isBipartite(self, graph: List[List[int]]) -> bool:
        """
        >>> Graph Painting for graph bipartite
        
        Use 1, 2 for different colors.
        """
        color = collections.defaultdict(int)
        valid = True
        def dfs(node):
            nonlocal valid
    
            for adj in graph[node]:
                # same color for one edge
                if color[adj] == color[node]:
                    valid = False
                else:
                    if color[adj] == 0:
                        color[adj] = -color[node]
                        dfs(adj)
        
        # traverse each unvisited node
        for node in range(len(graph)):
            if not color[node]:
                color[node] = 1
                dfs(node)
                
        return valid
