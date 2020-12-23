def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        """
        >>> recursion with memorization
        
        Normally I come up with a dp solution from the naive idea
        of brute force(dp is actually brute force with memorization);
        For this question, first I though it would be solved by trie but requires
        a lot of space if the wordDict is large. Then how about using memorized 
        recursion? And the attributes of the recursive function should be 
        the starting idx(since the whole s should be valid, there will be no
        end idx constraint).
        
        >>> dynamic programming
        
        From top-down to bottom-up, use an array dp to store the result.
        However, since it goes the opposite way, the idx should indicates
        whether s[:idx+1] is valid or not.
        """
        
        wordDict = set(wordDict)
        
        @lru_cache(None)
        def is_valid(start):
            if start == len(s):
                return True
            
            valid = False
            for i in range(start+1, len(s)+1):
                if s[start: i] in wordDict:
                    valid = valid | is_valid(i)
            
            return valid
        
        return is_valid(0)
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = [False] * (len(s)+1)
        dp[0] = True
        
        for i in range(1, len(s)+1):
            for j in range(i):
                dp[i] = dp[i] | (dp[j] & (s[j:i] in wordDict))
                if dp[i]: break
        
        return dp[-1]
