def eatenApples(self, apples: List[int], days: List[int]) -> int:
        """
        >>> Greedy
        
        Find the maximum days that you can eat apples from current day to all the
        days end before the last day.
        Also, we want to make sure we eat the apples that are earliest rotten, 
        therefore, the trick here is really just the usage of heap.
        """
        ans = i = 0
        heap = []
        while i < len(apples) or heap:
            if i < len(apples) and apples[i] > 0:
                heapq.heappush(heap, [i+days[i], apples[i]])
            
            # no eatable apples, pop the heap
            while heap and (heap[0][0] <= i or heap[0][1] == 0):
                heapq.heappop(heap)
            
            if heap:
                ans += 1
                heap[0][1] -= 1
            
            i += 1
        
        return ans
