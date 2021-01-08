def maxEvents(self, events: List[List[int]]) -> int:
        """
        >>> Greedy
        
        Add the events to the min heap and always attend the event that ends 
        earliest if possible.
        """
        events.sort(reverse=True)
        heap = []
        ans, curDay = 0, 0
        while events or heap:
            # if heap is empty, this suggest we have no events to attend
            # therefore to avoid unnecessary loop, we can directly jump
            # into next closest date that has events
            if not heap: curDay = events[-1][0] 
                
            # add the events to the heap
            while events and events[-1][0] == curDay:
                heapq.heappush(heap, events.pop()[1])
                
            heapq.heappop(heap)
            ans += 1
            curDay += 1
            
            # pop expired events
            while heap and heap[0] < curDay:
                heapq.heappop(heap)
        
        return ans
