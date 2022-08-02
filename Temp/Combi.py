class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.answer = []
        self.acc = []
        self.n = n
        self.k = k

        self.backTracking()

        return self.answer

    def backTracking(self):
        if len(self.acc) == self.k:
            temp = self.acc.copy()
            self.answer.append(temp)
            return

        for i in range(self.n):
            self.acc.append(i)

            self.backTracking()

            self.acc.pop()
        return

n = 4
k = 2
solution = Solution()
print(solution.combine(n, k))