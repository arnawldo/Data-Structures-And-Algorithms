# uses python3

'''
Checking for balanced parentheses in code
'''
import sys

def check_brackets(stringy):
    '''
    Input: string of length <= 1 consisting of big and small latin letters,
    digits, punctuation marks and brackets from the set []{}().

    Output: If the code in S uses brackets correctly, output “Success"
    (without the quotes). Otherwise, output the 1-based index of the first
    unmatched closing bracket, and if there are no unmatched closing brackets,
    output the 1-based index of the first unmatched opening bracket.
    '''
    # create stack for brackets
    stack = []
    # iterate though stringy
    for indx, character in enumerate(stringy):
        # if character is an opening bracket
        if character in '[{(':
            # push character and its position to stack
            stack.append((character, indx + 1))
            continue
        # if character is closing bracket and stack is non empty
        if character in ']})' and len(stack):
            if character == ']':
                if stack[-1][0] != '[':
                    # return position of unmatched closing bracket
                    return indx + 1
                else:
                    del stack[-1]
            elif character == '}':
                if stack[-1][0] != '{':
                    # return position of unmatched closing bracket
                    return indx + 1
                else:
                    del stack[-1]
            else:
                if stack[-1][0] != '(':
                    # return position of unmatched closing bracket
                    return indx + 1
                else:
                    del stack[-1]
        # if character is closing bracket and stack is non empty
        elif character in ']})' and not len(stack):
            # return position of unmatched closing bracket
            return indx + 1
    # check if any unmatched opening brackets exist
    if len(stack):
        # return position of last unmatched opening bracket
        return stack[-1][1]
    else:
        return 'Success'

if __name__ == '__main__':
    S = sys.stdin.read()
    print(check_brackets(S))
