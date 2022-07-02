import unittest

# Bowling - Recursive

def bowl_recursive(values):

    memo = {}

    def dp(i):
        if i >= len(values) - 1: return 0
        if i not in memo:
            memo[i] = max(dp(i+1), values[i] + dp(i+1), values[i]*values[i+1] + dp(i+2))
        return memo[i]
    
    return dp(0)


# Bowling - Iterative

def bowl_iterative(values):

    dp = {}
    dp[len(values)-1] = 0
    dp[len(values)] = 0

    for i in reversed(range(len(values)-1)):
        dp[i] = max(dp[i+1], dp[i+1] + values[i], dp[i+2] + values[i]*values[i+1])
    
    return dp[0]


test_case = [-1, 1, 1, 1, 9, 9, 3, -3, -5, 2, 2]

class TestCases(unittest.TestCase):
    def test_case1(self):self.assertEqual(bowl_recursive(values=test_case), 106)
    def test_case2(self):self.assertEqual(bowl_iterative(values=test_case), 106)

if __name__ == '__main__':
    unittest.main(verbosity=3, exit=False)