# Sample Test Case
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
# ["This    is    an","example  of text","justification.  "]
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16

# Microsoft Word uses greedy algo 
# LATEX uses dp solution

# Idea is to reduce the badness of a line
# b(i, j) = (s - (wi + ... + wj)^3) if s > (sum from i to j) else 'inf'

class Solution(object):

    def fullJustify_recursive(self, words, maxWidth):

        memo = {len(words):0}
        pointer = [-1 for _ in range(len(words))]

        # Calculate badness
        def b(i, j):
            value = (maxWidth - sum([len(x) for x in words[i:j+1]]))**3
            # print(value)
            return value if value >= 0  else float('inf')

        
        def dp(i):

            if i not in memo:
                minimum = float('inf')
                # memo[i] = min(b(i,j) + dp(j+1) for j in range(i,len(words)))

                for j in range(i, len(words)):
                    value = b(i,j) + dp(j+1)
                    if value < minimum:
                        minimum = value
                        pointer[i] = j
                        memo[i] = value

            return memo[i]
        
        dp(0)
        print(memo)
        print(pointer)

        i = 0
        while i < len(words):
            next = pointer[i]
            print(words[i:next+1])
            i = next + 1


if __name__ == '__main__':
    s = Solution()

    print(s.fullJustify_recursive(words, maxWidth))