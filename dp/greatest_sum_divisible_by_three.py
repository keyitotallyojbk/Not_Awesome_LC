def maxSumDivThree(self, nums: List[int]) -> int:
        """
        >>> dynamic programming
        
        Some dp problems can be tricky to identified, just like this,
        where we represent their state by a memorized array.
        """
        dp = [0, 0, 0]
        
        for idx in range(len(nums)):
            # using [:] is pretty tricky, basically it creates a duplicate of dp
            # for the current iteration
            for v in dp[:]:
                dp[(v+nums[idx]) % 3] = max(dp[(v+nums[idx]) % 3], nums[idx]+v)
        
        return dp[0]
