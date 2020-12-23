def maxResult(self, nums: List[int], k: int) -> int:
        """
        >>>Mono-deque
        
        The idea is, we only care about the path that has
        the largest scores, since we will all start from that
        in order to achieve global maximum. Therefore it is equivalent
        to track the largest score within the last k elements. So maintain
        a score array where score[i] indicates maximum score we 
        can get at index i
        """
        score = [0] * len(nums)
        score[0] = nums[0]
        max_win = collections.deque([0])
        for i in range(1, len(nums)):
            score[i] = score[max_win[0]] + nums[i]
            while max_win and score[i] > score[max_win[-1]]:
                max_win.pop()
            max_win.append(i)
            while (i-max_win[0]) >= k:
                max_win.popleft()
        
        return score[-1]
