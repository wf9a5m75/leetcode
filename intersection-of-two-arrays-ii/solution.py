class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # If nums1 and nums2 are already sorted, this work

        nums1.sort()
        nums2.sort()

        i1 = i2 = 0
        n1 = len(nums1)
        n2 = len(nums2)
        results = []
        while(i1 < n1) and (i2 < n2):

            if nums1[i1] == nums2[i2]:
                results.append(nums1[i1])
                i1+=1
                i2+=1
            elif (nums1[i1] < nums2[i2]):
                while(i1 < n1) and (nums1[i1] < nums2[i2]):
                    i1 +=1
            else:
                while(i2 < n2) and (nums1[i1] > nums2[i2]):
                    i2 +=1
        return results
