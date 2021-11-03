res = []


class Solution(object):
    def subsets(self, a):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        global arr
        arr = [-1 for i in range(len(a))]
        self.find_subsets(0, a)
        return res

    def find_subsets(self, index, a):
        if index == len(a):
            ls = []
            for i in range(len(arr)):
                if arr[i] == 1:
                    ls.append(a[i])
            res.append(ls)
            return
        arr[index] = 0
        self.find_subsets(index + 1, a)
        arr[index] = 1
        self.find_subsets(index + 1, a)

if __name__ == "__main__":
    obj = Solution()
    print(obj.subsets([1,2,3]))
