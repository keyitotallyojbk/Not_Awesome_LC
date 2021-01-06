??? from here until ???END lines may have been inserted/deleted
def triangleNumber(self, nums: List[int]) -> int:
        """
        >>> linear scan
        
        It is very intuitive to use binary search, which yields O(N^2log(N)) complexity.
        However, when we want to search for a larger side, we can start from the last previous
        side that satisfied the condition. This solution has only O(N^2) complexity.
        """
        ans = 0
        nums.sort()
        for i in range(len(nums)-2):
            lo = i
            if nums[i] == 0: continue
            for j in range(i+1, len(nums)-1):
                # linear scan to find the largest side
                target = nums[i]+nums[j]
                # since we know for a fixed first side, if we increase the second side,
                # all the previous third sides are valid, thus we do not have to start
                # from j, but from idx of the last third side.
                while lo+1 < len(nums) and nums[lo+1] < target:
                    lo += 1
                ans += lo-j
        
        return ans


def triangleNumber(self, nums: List[int]) -> int:
        """
        >>> three pointer 

        Similar to 3Sum problem, fix the largest side k, find the valid two sides that the sum
        of them should be larger than nums[k]
        """
        ans = 0
        nums.sort()
        for k in range(n-1,1,-1):
            lo = 0
            hi = k - 1
            while lo < hi:
                # valid two sides
                if nums[hi]+nums[lo] > nums[k]:
                    ans += hi-lo # all the lo to hi are valid
                    hi -= 1
                # otherwise move left pointer
                else:
                    lo += 1
        return ans
