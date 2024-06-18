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

def main():
    # Example usage
    nums = [3, 2, 2, 3]
    val = 3
    k = removeElement(nums, val)

if __name__ == "__main__":
    main()

