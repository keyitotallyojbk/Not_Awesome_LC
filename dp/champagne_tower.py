def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        """
        >>> DP
        
        The tricky part is, instead of reducing poured by the number of champagnes
        every time, we keep tracking the total cups of champagne that
        flow through each cup. And if it's greater than 1, both of the downward
        cups got the same amount of extra champagne.
        """
        dp = [[0]*k for k in range(1, 102)]
        dp[0][0] = poured
        for i in range(query_row+1):
            for j in range(i+1):
                q = (dp[i][j]-1) / 2
                if q > 0:
                    dp[i+1][j] += q
                    dp[i+1][j+1] += q
        
        return min(1, dp[query_row][query_glass])
