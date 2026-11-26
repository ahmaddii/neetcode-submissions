class Solution:

    def encode(self, strs: List[str]) -> str:
        res = "" # converting list of string into single string

        for s in strs:
            res += str(len(s)) + "#" + s # first putting int then pound then string value so that in decode we can simply get the int and then pound value after that we simple get it
        return res

    def decode(self, s: str) -> List[str]:

        res,i = [],0

        while i < len(s): # will read one word
            j = i

            while s[j] != "#": # jab tak pound tak nhi ate means int end nhi howa tab tak increment karo
                j += 1
            length = int(s[i:j])

            res.append(s[j+1 : j+1 + length])
            i = j + 1 + length 
        return res
            
          # we update i pointer to read next word

            # we start with j + 1 means after pound until and up to lenght of string
            
             # not including j this gives us int

# so now j tell us how many chars we have to read after j like pounda


solution = Solution()

strs = ["hello", "world", "#", "", "python"]

encoded_string = solution.encode(strs)
print(encoded_string)

decoded_string = solution.decode(encoded_string)
print(encoded_string)

