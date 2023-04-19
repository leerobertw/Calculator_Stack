from stack import Stack

operators = ('+', '-', '*', '/', '**')


def main():
    stack = Stack()
    val = ""
    while val != "done":
        val = input(">> ").strip()
        if val.isnumeric():
            stack.push(float(val))
            print(stack.display())
        elif val in operators:
            second = stack.pop()
            first = stack.pop()
            result = execute(first, second, val)
            stack.push(result)
            print(f"{first} {second} {val} is {result}")
            print(f"Current stack: {stack.display()}")


def execute(operand1, operand2, operator):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2
    elif operator == '**':
        return operand1 ** operand2


if __name__ == '__main__':
    main()
