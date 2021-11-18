# return sum of 3 numbers that is close to target.
class Solution:
    def threeSumClosest(self, nums, target):
        diff = float('inf')
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    diff01 = abs(target - (nums[i] + nums[j] + nums[k]))
                    if diff01 < diff:
                        diff = diff01
                        sum = nums[i] + nums[j] + nums[k]
        return sum

if __name__ == "__main__":
    nums = [1, 1, 1, 0]
    target = -100
    obj = Solution()
    print(obj.threeSumClosest(nums, target))