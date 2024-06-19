class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = 0 
        for next in range(1, len(nums)):
            if nums[prev] != nums[next] :
                prev += 1
                nums[prev] = nums[next]
    
        return prev + 1 
