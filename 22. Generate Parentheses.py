from typing import List
# def generateParenthesis(n: int) -> List[str]:
    # ["((()))","(()())","(())()","()(())","()()()"]
        
    # return

# print(generateParenthesis(n=3))


# back_tracking(path,options):
#     if base_case:
#         # add path to result
#         retur
    
#     for option in options:
#         if is valid(option):
#             path.append(option)
#             backtrack(path,new_option)
#             path.pop()
            
# n = 3 - ["((()))","(()())","(())()","()(())","()()()"]
# Candidates: What are the possible choices at each step? - '(' or ')'
# Constraints: What conditions must be met for a choice to be valid? 
    # - no of '(' is less than n
    # - at any point no of closing parenthesis is less than no of '('
                                                                    
# Goal: What is the condition that indicates a complete solution? 
    # no of '(' = no of ')'

def generateParenthesis(n: int) -> List[str]:

    def back_tracking(path,open_count,close_count):
        if len(path) == 2*n:
            res.append(path)
            return
        
        if open_count < n:
            back_tracking(path+'(',open_count+1,close_count)
        if close_count < open_count:
            back_tracking(path+')',open_count,close_count+1)
        
    res = []
    back_tracking("",0,0) # path : current sequenc of pattern, options: the next choic of sequence
    return res

print(generateParenthesis(n=3))