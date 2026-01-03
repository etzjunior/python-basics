class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n

        # ways for step 1 and step 2
        prev2 = 1  # f(1)
        prev = 2   # f(2)

        # f(i) = f(i-1) + f(i-2)
        for _ in range(3, n + 1):
            curr = prev + prev2
            prev2 = prev
            prev = curr

        return prev
