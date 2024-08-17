from typing import List
def letterCombinations(digits: str) -> List[str]:
    if not digits:
        return []
    
    dict = {
        2:'abc',
        3:'def',
        4:'ghi',
        5:'jkl',
        6:'mno',
        7:'pqrs',
        8:'tuv',
        9:'wxyz'
    }

    result = []
    
    def backtrack(index,path):
        if len(path) == len(digits):
            result.append(path)
            return 

        letters = dict[int(digits[index])]
        for l in letters:
            print(l)
            backtrack(index+1,path+l)
        
    backtrack(0, "")
    return result

digits = "23"
print(letterCombinations(digits))
