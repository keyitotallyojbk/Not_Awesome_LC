def minCameraCover(self, root: TreeNode) -> int:
        """
        >>> Greedy/DFS
        
        The idea is, if a node has all children monitored and it
        has parent, it's alway better to put a camera at its parent.
        We do not add camera if:
            1. Both children are monitored and one is camera;
            2. Both children are monitored and if has a parent
        Otherwise we should add a camera at current node.
        """
        ans = 0
        def dfs(node, parent=None):
            """
            DFS function should return whether the current node is
            monitored or not
            """
            nonlocal ans
            if not node or node.val == 1: return True
            
            if (dfs(node.left, node)+dfs(node.right, node))==2:
                if node.left:
                    if node.left.val == 1: return True
                if node.right:
                    if node.right.val == 1: return True
                if parent:
                    return False
            
            node.val = 1
            ans += 1
            return True
        
        dfs(root)
        
        return ans
