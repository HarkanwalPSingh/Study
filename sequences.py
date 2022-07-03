# Sequence - Recursive

def seq_generator_rec(values):

    memo = {len(values):['']}

    def dp(i):

        if i not in memo:
            memo[i] = [values[i]+value for value in dp(i+1)]
            memo[i].extend([value for value in dp(i+1)])
            # print(memo)
        
        return memo[i]
    
    return dp(0)


# Sequence - Iterative

def seq_generator_iterative(values):

    dp = {}
    dp[len(values)] = ['']

    for i in reversed(range(len(values))):
        dp[i] = [values[i] + value for value in dp[i+1]]
        dp[i].extend([value for value in dp[i+1]])
    
    return dp[0]


def seq_generator_optimum(values):

    dp = ['']

    for i in reversed(range(len(values))):
        temp = [values[i] + value for value in dp]
        temp.extend([value for value in dp])
        dp = temp
    
    return dp


test_case = 'ABCD'

# print(seq_generator_rec(test_case))
# print(seq_generator_iterative(test_case))
print(seq_generator_optimum(test_case))