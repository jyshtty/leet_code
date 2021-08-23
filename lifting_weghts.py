"""
https://leetcode.com/discuss/interview-question/858129/roblox-oa-new-grad-2021
"""


def weightCapacity(weights, maxCapacity):
    max_sum = set([0])
    for weight in weights:
        temp = set([0])
        for i in max_sum:
            if weight + i == maxCapacity:
                return maxCapacity
            elif (weight + i) < maxCapacity:
                temp.add(weight + i)
        max_sum.update(temp)
    return max(max_sum)
