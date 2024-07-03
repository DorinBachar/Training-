class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        num = 0
        for index in range(len(nums)):
            if nums[index] != val:
                nums[num] = nums[index]
                num += 1
        return num


