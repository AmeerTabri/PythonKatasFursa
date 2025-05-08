def is_valid_parentheses(s):
    close_to_open = {')': '(', ']': '[', '}': '{'}
    stack = []
    for char in s:
        if char in close_to_open:
            if not stack or close_to_open[char] != stack[-1]:
                return False
            else:
                stack.pop()
        else:
            stack.append(char)

    return not stack


if __name__ == '__main__':
    valid_input = "()[]{}"
    invalid_input1 = "(]"
    invalid_input2 = "([)]"
    valid_input_nested = "{[]()}"

    print(f"'{valid_input}' has valid parentheses: {is_valid_parentheses(valid_input)}")  # Should be True
    print(f"'{invalid_input1}' has valid parentheses: {is_valid_parentheses(invalid_input1)}")  # Should be False
    print(f"'{invalid_input2}' has valid parentheses: {is_valid_parentheses(invalid_input2)}")  # Should be False
    print(f"'{valid_input_nested}' has valid parentheses: {is_valid_parentheses(valid_input_nested)}")  # Should be True
