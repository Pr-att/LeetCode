# s = "()[]{}"
# s = "(){}[]"
# s = '}{{'
def parentheses():
    s = '((({{[]}}))))'
    stack = []
    hash_map = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    opposite = {']', ')', '}'}

    for i in s:
        if i in hash_map:
            stack.append(hash_map[i])
        elif i in opposite:
            if not stack or stack.pop() != i:
                return False

    return len(stack) == 0


print(parentheses())
