class Solution:
    def solve(self,A):
        for i in range(len(A)):
            if A[i] >= len(A) and A[i] != (i):
                i, A[i] = A[i], i
        for i in range(len(A)):
            if A[i] != i: return i
        return len(A) # if A = [0,1,2,3] this line will return 4

