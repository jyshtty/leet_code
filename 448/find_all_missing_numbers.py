def findDisappearedNumbers(nums):
    new = []
    nums.sort()
    i = 1
    k = 0
    while i <= len(nums):
        if i != nums[i - 1 + k] and i > nums[i - 1 + k] and i == len(nums):
            new.append(i)
            break
        if i != nums[i - 1 + k] and i < nums[i - 1 + k]:
            new.append(i)
            k -= 1
        elif i != nums[i - 1 + k] and i > nums[i - 1 + k]:
            k += 1
        i += 1
    return new

print(findDisappearedNumbers([1,1,2,2]))