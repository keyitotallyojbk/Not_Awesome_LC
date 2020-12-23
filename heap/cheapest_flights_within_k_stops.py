def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        """
        >>> Dijkstra's Algorithm Variation
        
        The differences are:
        1. Also track the number of stops so far;
        2. Now since we have a stop limitation, the distances are not strictly
        minimal, so we cannot avoid traversing the same point;
        """
        # build graph first
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append([v, w])
            
        dist = {}
        q = [(0, src, -1)] # tuple of (dist, node, num_stops)
        while q:
            d, node, num_stops = heapq.heappop(q)
            if node not in dist: dist[node] = d # now we cannot stop here
            if node == dst: return d
            num_stops += 1
            if num_stops > K: continue
            for adj, w in graph[node]:
                heapq.heappush(q, (d+w, adj, num_stops)) # despitethe node has been visited, we still need to traverse from it
        
        return -1
