def largestRectangleArea(self, heights: List[int]) -> int:
        """
        >>>Very typical mono stack method

        There are two ways to solve this problem:
        1. Three-pass; two mono-stack; easier to understand
        and implement;
        2. One-pass, one mono-stack; need special initialization.
        """
        
        if not heights:
            return 0
        
        # maintain a mononically increase stack(not strictly)
        area = 0
        mono = [-1] # this is of vital importance for one-pass method
        for i in range(len(heights)):
            while len(mono)>1 and heights[mono[-1]] > heights[i]:
                idx = mono.pop()
                area = max(area, (i-mono[-1]-1)*heights[idx])
            
            mono.append(i)
        
        while len(mono)>1:
            idx = mono.pop()
            area = max(area, (len(heights)-mono[-1]-1)*heights[idx])
                
        return area
