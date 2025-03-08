"""
Given an input, we ask for the following Output

Input: "hello" -> Output: "olleh" 
Input: "Python" -> Output: "nohtyP"
"""



""" Solution """
#"""
def reverse_strings(input: str) -> str:
    result = ""
    for i in range(-1,-(len(input)+1),-1):
        result += input[i]
    return result
#"""


""" Solution with reversed """
"""
def reverse_strings(input: str) -> str:
    result = ""
    return result.join(reversed(input))
"""


""" Solution with reversed """
"""
def reverse_strings(input: str) -> str:
    return input[::-1]
"""