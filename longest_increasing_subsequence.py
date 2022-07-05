"""
A = carbohydrate
Solution: abort -> 5
"""

# SRTBOT
# Subproblems: x(i) = lis in A[i:]
# Relate: x(i) = max(1 + x(j)) | where i<j<|A| & A[i] < A[j]
# Topo order: i in decreasing order
# Base: -
# Original problem: max(x) first element of the subsequence could be anyone from the sequence
# Time complexity: O(|A|**2)

def lis(A):
    n = len(A)
    
    x = [1 for _ in range(n)]

    for i in reversed(range(n)):
        for j in range(i,n):
            if A[i] < A[j]:
                x[i] = max(x[i], 1 + x[j])
    
    return max(x)

if __name__ == '__main__':
    A = "carbohydrate"
    print(lis(A))
