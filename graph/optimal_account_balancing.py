def minTransfers(self, transactions: List[List[int]]) -> int:
        """
        >>> DFS
        
        This is an N-P complete problem with two steps:
            1. construct a debit list
            2. dfs on searching the minimum step transactions
        After we've completed the current debit, search on
        the minimum steps from the second non-zero debit.
        """
        debit = collections.defaultdict(int)
        for trans in transactions:
            debit[trans[0]] -= trans[2]
            debit[trans[1]] += trans[2]
        debit = list(debit.values())
        
        def dfs(p):
            while p < len(debit) and debit[p] == 0:
                p += 1
            if p >= len(debit):
                return 0
            
            min_trans = float('inf')
            for i in range(p+1, len(debit)):
                if debit[i]*debit[p] < 0:
                    debit[i] += debit[p]
                    min_trans = min(min_trans, 1+dfs(p+1))
                    debit[i] -= debit[p]
                
            return min_trans
        
        return dfs(0)
