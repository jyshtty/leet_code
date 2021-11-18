class Solution:
    def isHappy(self, n):
        visited = set()
        while n not in visited:
            visited.add(n)
            n = self.sumOfSquaresOfNums(n)
            if n == 1:
                return n == 1
        return False

    def sumOfSquaresOfNums(self, n):
        sum = 0
        while n:
            rem = n % 10
            sum = sum + rem ** 2
            n = n / 10
        return sum

if __name__ == "__main__":
    obj = Solution()
    print(obj.isHappy(19))