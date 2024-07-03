class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1  # Base case: there's one way to stay at the ground (doing nothing).
    
    # Initialize dp array with base cases
        dp = [0] * (n + 1)
        dp[0] = 1  # There's one way to stay at ground (doing nothing)
        dp[1] = 1  # There's one way to reach the first step (taking one step)
    
    # Compute dp values up to dp[n]
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
    
        return dp[n]    
