from typing import List
# def longestCommonPrefix(strs: List[str]) -> str:
        # strs.sort()
        # wf = strs[0]
        # wl = strs[len(strs)-1]

        # ans = ""
        # for i in range(min(len(wf),len(wl))):
        #     if wf[i]!=wl[i]:
        #         return ans
        #     ans+=wf[i]        
        # return ans

def longestCommonPrefix(strs: List[str]) -> str:
        
        if not strs:
            return ""
        
        prefix = strs[0]
        
        for i in range(1,len(strs)):
            while strs[i][:len(prefix)] != prefix:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix
            
# TC: O(n*m), where n is length of the strs and m is the prefix size
        
strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))

# O(nlogn+m)
# where n is the anumber of strings and m is the length of the shortest string.