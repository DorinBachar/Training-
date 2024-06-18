class Solution(object):
    def merge(self, nums1, m, nums2, n):
        index1, index2 , index = m - 1, n - 1 , m + n -1

        while index2 >= 0:
            if index1 >=0  and  nums1[index1] > nums2[index2] :
                nums1[index] = nums1[index1]
                index1 -= 1
            else:
                nums1[index] = nums2[index2]
                index2 -= 1
            index -= 1



def main() :
    nums1 = [1, 2, 3]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    merge(nums1, m, nums2, n)
    print(nums1) 


  
