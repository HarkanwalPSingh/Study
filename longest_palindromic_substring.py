import collections


def palindromic_substring(word):

    memo = {}

    def dp(i,j):

        if i>j: return 0

        if i == j: return 1

        key = (i,j)

        if key not in memo:
            memo[key] = 2 + dp(i+1,j-1) if word[i]==word[j] else max(dp(i+1,j), dp(i,j-1))
        
        return memo[key]
    
    return dp(0,len(word)-1)


test_case = "bazaaraavoice"

# print(palindromic_substring(test_case))


def longest_palindrome_brute_force(word):

    # Helper Function
    def isPalindrome(word,i,j):
        l, r = i, j

        while l <= r:
            
            if word[l] != word[r]:
                return False
            
            l += 1
            r -= 1
        
        return True

    
    result = [[] for i in range(len(word))]


    for i in range(len(word)):
        for j in range(i+1, len(word)):
            # print(word)
            if isPalindrome(word, i, j):
                result[j-i].append(word[i:j+1])
    
    # print(result)

    for i in reversed(range(len(result))):
        if len(result[i]) > 0:
            return result[i][-1]

def longest_palindrome_expand_from_centre(word):

    left, right = 0, 0
    resLen = -1

    for i in range(len(word)):

        # Odd length Palindrome
        l, r = i, i
        while l >= 0 and r < len(word) and word[l] == word[r]:
            if (r - l + 1) > resLen:
                left, right = l, r
                resLen = r - l + 1
            
            l -= 1
            r += 1
        

        # Even length Palindrome
        l, r = i, i+1
        while l >= 0 and r < len(word) and word[l] == word[r]:
            if (r - l + 1) > resLen:
                left, right = l, r
                resLen = r - l + 1
            
            l -= 1
            r += 1
        
    return word[left: right+1]

# print(longest_palindrome_brute_force(test_case))
print(longest_palindrome_expand_from_centre(test_case))