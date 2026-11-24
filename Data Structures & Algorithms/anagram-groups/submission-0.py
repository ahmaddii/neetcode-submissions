class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list) # created empty resource list

        for s in strs:
            sorteds = "".join(sorted(s)) ## means a e f into aef
            res[sorteds].append(s)
            
        return list(res.values())


        