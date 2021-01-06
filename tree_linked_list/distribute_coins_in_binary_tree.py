def distributeCoins(self, root: TreeNode) -> int:
        num_opt = 0
        def dfs(node):
            """
            >>> DFS
            
            Traverse the tree, for each node, the number of moves
            is the absolute values between 1 and the left/right node
            values. Also remember to update the node values.
            """
            nonlocal num_opt
            
            if not node: return 1
            L, R = dfs(node.left), dfs(node.right)
            num_opt += abs(L-1)+abs(R-1)
            node.val += L+R-2
            return node.val
        
        dfs(root)
        
        return num_opt
