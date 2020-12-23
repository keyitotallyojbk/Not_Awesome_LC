def maxProduct(self, nums: List[int]) -> int:
        """
        We need to track the max_prod and min_prod since 
        a maximum can be yield when by max_prod*n where n > 0
        or min_prod *n where n < 0
        """
        max_prod, min_prod = nums[0], nums[0]
        ans = max_prod
        
        for n in nums[1:]:
            if n > 0:
                max_prod, min_prod = max(n, max_prod*n), min(n, min_prod*n)
            elif n < 0:
                max_prod, min_prod = max(n, min_prod*n), min(n, max_prod*n)
            else:
                max_prod, min_prod = 0, 0
            
            ans = max(max_prod, ans)
            
        return ans
