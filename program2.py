def decode_message(s: str, p: str) -> bool:
    # Get lengths of the string and pattern
    m, n = len(s), len(p)
    
    # Create a DP table with dimensions (m+1) x (n+1)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    # Base case: empty string and empty pattern match
    dp[0][0] = True
    
    # Base case: pattern can match an empty string if it's all '*'
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
    
    # The answer is in dp[m][n], i.e., whether the entire string matches the pattern
    return dp[m][n]