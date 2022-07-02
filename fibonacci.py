import unittest

# Fibonacci Numbers - Recursive

def fib_recursive(n):
    memo = {0:1, 1:1}

    def dp(i):

        if i not in memo:
            memo[i] = dp(i-1) + dp(i-2)

        return memo[i]
    
    return dp(n)


# Fibonacci Numbers - Iterative

def fib_iterative(n):

    dp = {0:1, 1:1}

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]


# Fibonacci Numbers - Optimisation

def fib_optimum(n):

    num1, num2 = 1, 1

    for i in range(2, n+1):
        num1, num2 = num2, num1 + num2
    
    return num2

class TestCases(unittest.TestCase):
    def test_case1(self): self.assertEqual(fib_iterative(10), 89)
    def test_case2(self): self.assertEqual(fib_recursive(10), 89)
    def test_case3(self): self.assertEqual(fib_optimum(10), 89)


if __name__ == '__main__':
    unittest.main(verbosity=3, exit=False)