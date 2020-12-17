def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        """
        >>>Implementation of Dijkstra's algorithm using priority queue
        
        This is basically a greedy way to find the shortest distance:
        We start from the source, greedily find the closest node and 
        then update the distances to its all adjacents. The tricks are:
        1. Initialize the heap with the source and dynamically add adjacent
        nodes;
        2. Using dictionary to store the current distances, this can be done
        since we know all the keys in it have been visited and the distances
        are already minimum so that need not to be updated;
        3. If we want to find the shortest distance from src to a specific
        target, simply add a if loop.
        """
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))
            
        dist = {}
        q = [(0, K)]
        
        while q:
            w, u = heapq.heappop(q)
            if u in dist: continue
            dist[u] = w
            for d, v in graph[u]:
                if v not in dist:
                    heapq.heappush(q, (dist[u]+d, v))
        
        return max(dist.values()) if len(dist) == N else -1
