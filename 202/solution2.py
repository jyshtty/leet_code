class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            visited.add(n)
            n = self.sumOfSquaresOfNums(n)
            if n == 1:
                return True
        return False

    def sumOfSquaresOfNums(self, n):
        return sum([int(c) * int(c) for c in str(n)])