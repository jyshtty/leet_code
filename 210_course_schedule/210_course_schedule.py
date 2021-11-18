# class Solution:
#     # prerequisites = [[1,0],[2,0],[3,1],[3,2]]
#     def findOrder(self, numCourses, prerequisites):
#         dict01 = {}
#         indegree = dict((i,0) for i in range(numCourses))
#         output = []
#         for i in range(len(prerequisites)):
#             if prerequisites[i][1] not in dict01:
#                 dict01[prerequisites[i][1]] = [prerequisites[i][0]]
#             else:
#                 dict01[prerequisites[i][1]].append(prerequisites[i][0])
#             indegree[prerequisites[i][0]] = indegree[prerequisites[i][0]] + 1
#
#         quque = [-100]
#         while len(quque) != 0:
#             if -100 in quque:
#                 quque.remove(-100)
#
#             for i in indegree:
#                 if indegree[i] == 0:
#                     if i not in quque:
#                         quque.append(i)
#             # new_quque = list(quque)
#
#             for i in quque:
#                 if indegree[i] == 0:
#                     del indegree[i]
#                     if i in dict01:
#                         # new_quque.extend(dict01[i])
#                         quque.extend(dict01[i])
#                         for j in dict01[i]:
#                             indegree[j] -= 1
#             quque = list(set(new_quque))
#
#             temp = list(quque)
#             for i in quque:
#                 if i not in indegree:
#                     temp.remove(i)
#                     output.append(i)
#             quque = list(temp)
#         return output
#
# if __name__ == "__main__":
#     # numCourses = 4
#     # prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
#     numCourses = 2
#     prerequisites = [[1, 0]]
#     obj = Solution()
#     print(obj.findOrder(numCourses, prerequisites))

# class Solution:
#     prev_mid = 0
#     def binary_search(self, arr, low, high, no_of_missing_number_at_mid, k, previous_iteration_missing_no):
#         while low <= high:
#             mid = low + ((high - low) // 2)
#             no_of_missing_number_at_mid = arr[mid] - mid - 1
#             if (previous_iteration_missing_no < k < no_of_missing_number_at_mid and ((self.prev_mid + 1) == mid))  :
#                 return arr[mid] - (no_of_missing_number_at_mid - k + 1)
#             if (((self.prev_mid - 1) == mid) and (previous_iteration_missing_no > k > no_of_missing_number_at_mid)):
#                 return arr[mid] + (k - no_of_missing_number_at_mid)
#             if (((self.prev_mid - 1) == mid) and (previous_iteration_missing_no > no_of_missing_number_at_mid > k)):
#                 low = low - 1
#                 previous_iteration_missing_no = no_of_missing_number_at_mid
#                 self.prev_mid = mid
#                 continue
#             previous_iteration_missing_no = no_of_missing_number_at_mid
#             self.prev_mid = mid
#             if k == no_of_missing_number_at_mid:
#                 return mid + k
#             elif k > no_of_missing_number_at_mid:
#                 low = mid + 1
#                 return self.binary_search(arr, low, high, no_of_missing_number_at_mid, k, previous_iteration_missing_no)
#             else:
#                 high = mid - 1
#                 return self.binary_search(arr, low, high, no_of_missing_number_at_mid, k, previous_iteration_missing_no)
#         else:
#             return arr[high] + k
#
#     def findKthPositive(self, arr, k):
#         previous_iteration_missing_no = 0
#         no_of_missing_number_at_mid = 0
#         high = len(arr) - 1
#         low = 0
#         return self.binary_search(arr, low, high, no_of_missing_number_at_mid, k, previous_iteration_missing_no)
#
#
# obj = Solution()
# # arr = [2]
# # k = 1
# arr = [1,10,21,22,25]
# k = 12
# print(obj.findKthPositive(arr, k))

class Solution:
    prev_mid = 0
    def binary_search(self, arr, low, high, k):
        if len(arr) == 1:
            if k < arr[0]:
                return k
            else:
                return k + 1
        mid = low + (high - low)//2
        if mid == 0 and k < arr[0]:
            return k
        no_of_missing_number_at_mid = arr[mid] - mid - 1
        if mid == len(arr)-1:
            return arr[mid] + k - no_of_missing_number_at_mid
        no_of_missing_number_at_mid_plus_one = arr[mid + 1] - (mid + 1) - 1
        no_of_missing_number_at_mid_minus_one = arr[mid - 1] - (mid - 1) - 1
        # if no_of_missing_number_at_mid == k:
        #     return arr[mid] - 1
        if no_of_missing_number_at_mid < k <= no_of_missing_number_at_mid_plus_one:
            return arr[mid] + (k - no_of_missing_number_at_mid)
        elif no_of_missing_number_at_mid_minus_one < k < no_of_missing_number_at_mid:
            return arr[mid-1] + (k - no_of_missing_number_at_mid_minus_one)
        elif k > no_of_missing_number_at_mid_plus_one:
            low = mid + 1
            return self.binary_search(arr, low, high, k)
        else:
            high = mid - 1
            return self.binary_search(arr, low, high, k)

    def findKthPositive(self, arr, k):
        high = len(arr) - 1
        low = 0
        return self.binary_search(arr, low, high, k)

    def findKthPositive(self, arr, k):
        high = len(arr) - 1
        low = 0
        return self.binary_search(arr, low, high, k)

obj = Solution()
# arr = [2]
# k = 1
# arr = [1,10,21,22,25]
# k = 12

# arr = [3,10]
# k = 2

arr = [1,5,6,7,12,14,17,32,35,43,55,60,64,65,67,75,79,80,82,90,92,93,95,99,102,103,109,110,111,112,113,114,129,132,134,139,141,146,147,152,162,163,164,172,183,200,202,206,216,217,219,222,223,231,232,241,246,260,261,262,276,278,285,294,302,303,305,306,312,323,325,331,332,333,337,341,344,345,352,353,361,369,378,383,396,403,406,408,409,415,418,419,422,427,433,437,438,441,444,447,448,456,460,461,464,471,476,480,482,483,485,487,490,491,493,497,499,506,507,509,511,513,518,522,528,530,531,532,535,536,539,543,548,551,552,553,556,563,567,572,578,579,586,587,588,589,590,594,607,611,613,617,619,627,629,632,636,638,650,654,659,667,669,672,673,675,676,682,685,693,705,710,714,717,724,727,728,729,732,740,743,752,763,766,771,772,777,784,787,793,799,800,804,805,811,822,826,838,840,848,850,851,857,859,863,864,865,868,872,873,880,883,887,891,893,895,902,906,908,909,915,918,922,926,931,933,948,953,959,962,965,967,972,973,976,983,984,985,986,989,993]
k = 71
print(obj.findKthPositive(arr, k))

# 19

