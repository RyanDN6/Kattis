s = input()

def backspace(s):

    stack = []

    for char in s:
        if char != "<":
            stack.append(char)
        else:
            stack.pop(-1)
    
    return "".join(stack)

print(backspace(s))
    
