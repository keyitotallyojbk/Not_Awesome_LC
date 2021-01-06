def isValidBST(self, root: TreeNode) -> bool:
        def valid(node, lb, rb):
            """
            node: current node
            lb: left bound
            rb: right bound
            """
            if not node: return True
            if node.val <= lb or node.val >= rb:
                return False
            
            return valid(node.left, lb, node.val) and valid(node.right, node.val, rb)
        
        return valid(root.left, float('-inf'), root.val) and valid(root.right, root.val, float('inf'))
