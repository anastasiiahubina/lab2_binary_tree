def is_balanced(sequence):
    stack = []
    brackets = {'(': ')', '[': ']', '{': '}'}
    
    for char in sequence:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return "NO"
    return "YES" if not stack else "NO"

# Зчитування вхідних даних
sequence = input().strip()
print(is_balanced(sequence))