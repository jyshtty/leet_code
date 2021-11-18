class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        result = 10**5
        for i in range(len(nums)-2):
            left_pointer = i+1
            right_pointer = len(nums)-1
            while (left_pointer < right_pointer):
                curr_sum = nums[i] + nums[left_pointer] + nums[right_pointer]
                if curr_sum < target:
                    left_pointer += 1
                else:
                    right_pointer -= 1
                if abs(target - curr_sum) < abs(target - result):
                    result = curr_sum
        return result

if __name__ == "__main__":
    nums = [-1,2,1,-4]
    target = 1
    obj = Solution()
    print(obj.threeSumClosest(nums, target))