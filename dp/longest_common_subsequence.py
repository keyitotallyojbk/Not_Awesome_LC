def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        >>> dynammic programming
        
        This question is known as LCS problem and is presented together with
        LIS: longest increasing subsequence.
        """
        # current solution can be optimized using O(N) space
        
        L1, L2 = len(text1), len(text2)
        dp = [[0] * L2 for _ in range(L1)]
        # initialization
        dp[0][0] = int(text1[0] == text2[0])
        for i in range(1, L1):
            dp[i][0] = min(dp[i-1][0] + int(text1[i] == text2[0]), 1)
        for j in range(1, L2):
            dp[0][j] = min(dp[0][j-1] + int(text1[0] == text2[j]), 1)
            
        # dp iteration
        for i in range(1, L1):
            for j in range(1, L2):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else: 
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]
