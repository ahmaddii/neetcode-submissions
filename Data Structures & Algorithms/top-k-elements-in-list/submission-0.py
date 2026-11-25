class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {} # emopty dict banai

        for num in nums:
            
            count[num] = count.get(num,0) + 1 # first come num is exist add 1 if not 0

        sorted_num = sorted(count,key=count.get,reverse=True)

            # by default it sorted the keys we are doing the values
            # hightest to lowest revese=true

        return sorted_num[:k] # means if we have 2 in sorted num 
            
            #[1,2,3 it gives = 1,2]