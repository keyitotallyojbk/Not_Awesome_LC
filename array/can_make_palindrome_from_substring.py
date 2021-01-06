def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        """
        >>> prefix sum problem!!!!!!!!!!!!!!!!
        Since we can rearrange the substring, the only thing we care about is 
        the frequency of them. Also, if we can replace some of them, we have to 
        find minimum number of replacement that makes the frequency of them to be 
        at most one odd number
        """
        count = [[0]*26]
        
        # The key idea is to store the count that yields O(26N) time complexity
        for i, ch in enumerate(s):
            count.append(count[i][:])
            count[i+1][ord(ch) - ord('a')] += 1
        
        ans = []
        
        for i, j, k in queries:
            min_opt = sum((count[j+1][ii]-count[i][ii]) % 2 for ii in range(26)) // 2
            if min_opt <= k:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans
