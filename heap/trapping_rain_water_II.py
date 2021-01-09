def trapRainWater(self, heightMap: List[List[int]]) -> int:
        """
        >>> heap
        
        Since the amount of water is only determined by the shortest 
        height, we should find that boundary first and do a BFS to find
        the amount of water we can trap. The key of the algorithm is:
            1. Start from the outer boundary;
            2. Usage of heap;
            3. Smallest boundary for current water trap.
        """
        ans, bound = 0, 0
        H, W = len(heightMap), len(heightMap[0])
        heap = []
        visited = [[0]*W for _ in range(H)]
        # start from the outer boundary
        for i in [0, H-1]:
            for j in range(W):
                if visited[i][j] == 0:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = 1
        for j in [0, W-1]:
            for i in range(H):
                if visited[i][j] == 0:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = 1
        
        # for each shortest height, find its neighbor
        while heap:
            height, row, col = heapq.heappop(heap)
            bound = max(bound, height)
            for r, c in [[row+1, col], [row-1, col], [row, col+1], [row, col-1]]:
                if 0 <= r < H and 0 <= c < W and visited[r][c] == 0:
                    ans += max(0, bound-heightMap[r][c])
                    heapq.heappush(heap, (heightMap[r][c], r, c))
                    visited[r][c] = 1
        
        return ans
