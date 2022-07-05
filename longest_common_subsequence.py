"""
A = hieroglyphology, B = michaelangelo
Result = hello or heglo or iello or ieglo, all length 5
"""

# SRTBOT
# Subproblems: x(i,j) = common subsequence of suffixes A[i:] and B[j:]
# Relate: x(i,j) = x(i+1,j+1) + 1 if A[i] = B[j] else max(x(i+1,j), x(i,j+1))
# Topo Order: i increases and/or j increases
# Base: x(i,|B|) = x(|A|,j) = 0
# Original Prob: x(0, 0), use parent pointers to reconstruct subsequence
# Time: O(|A|.|B|)

def lcs(A, B):
    a, b = len(A), len(B)
    x = [[0]*(b + 1) for _ in range(a+1)]

    for i in reversed(range(a)):
        for j in reversed(range(b)):
            if A[i] == B[j]:
                x[i][j] = x[i + 1][j + 1] + 1
            else:
                x[i][j] = max(x[i + 1][j], x[i][j + 1])
    
    for y in x:
        print(y)

    return x[0][0]

if __name__ == '__main__':
    A = "hieroglyphology"
    B = "michaelangelo"

    print(lcs(A, B))

    