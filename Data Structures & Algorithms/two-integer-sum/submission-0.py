class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)): # it run from i to range of arr
            for j in range(i+1,len(nums)): # i+1 move to next index
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []
# not optimal this brute force becuase of o(n2) when ever array is big we have to iterate everytime its too big