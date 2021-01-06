def lengthOfLIS(self, nums: List[int]) -> int:
        """
        >>> dynamic programming
        
        1. There could be a O(N^2) solution using DP, which is the one we used to solve
        longest common subsequence problem(LCS);
        
        >>> binary search
        2. However, for LIS problem, we have a O(Nlog(N)) solution with the help
        of binary search:
            - Maintain a piles arr of which piles[i] stores the smallest tail of length i
        """
        piles = []
        for num in nums:
            # for each number, do a binary search on which pile it should be added on 
            lo, hi = 0, len(piles)
            while lo < hi:
                mid = (lo+hi)//2
                if piles[mid] < num:
                    lo = mid+1
                else:
                    hi = mid
            # if the current number is greater than all the smallest pile tails, this means 
            # we can extend the largest pile with tail number
            if lo == len(piles):
                piles.append(num)
            # else we update the smallest tail for that pile since we now find a smaller tail
            # which is more likely to construct an increaing subsequence
            else:
                piles[lo] = num
        
        return len(piles)
