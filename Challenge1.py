"""
Given an input, we ask for the following Output

Input: "3[a]2[bc]" -> Output: "aaabcbc" 
Input: "3[a2[c]]" -> Output: "accaccacc"
"""




"""Solution"""
def string_obtainer(input: str) -> str:

    # It returns the inside of the brackets "[]", and multiplies for the int before the brackets.
    def recursive_function(index: int)-> list:
        result = ""
        num = 0
        while index < (len(input)):
            char = input[index]
            if char.isdigit():
                num = int(char)
            elif char == "[":
                # Obtain the string inside the brackets and the new index.
                sub_string, index = recursive_function(index+1)
                result += num*sub_string
                num = 0
            elif input[index] == "]":
                return result, index
            else:
                result += char
            index+=1
        return result, index
    final_result, _ = recursive_function(0)
    return final_result





# string_to_traduce = "3[a]2[bc]"
string_to_traduce = "3[a2[bc]]"
traduced_string = string_obtainer(string_to_traduce)
print(traduced_string)