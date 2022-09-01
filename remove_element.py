class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        for i in range(nums.count(val)):
            nums.remove(val)
            nums.sort()
        return nums

sorted = Solution().removeElement([3, 2, 2, 3], 3)
print(sorted)
        