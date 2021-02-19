# Evaluate whether the brackets are valid (){}[]

# sample input
in1 = "({[]})({[]}()[]{([])}"
in2 = "({[]}{[())]}()[]{([])}"
in3 = ""
in4 = " "


def isOpen(elem, brks):
    if elem in brks.keys():
        return True
    return False


def matches(elem, stack, brks):
    if brks.get(stack[-1]) == elem:
        return True
    return False


def isEven(inString):
    if len(inString) < 2:
        return False

    brk = {'(': ')', '{': '}', '[': ']'}

    stack = []

    for i in inString:
        if (isOpen(i, brk)):
            stack.append(i)
        else:
            if (len(stack) < 1 or not matches(i, stack[-1], brk)):
                return False
            stack.pop()

    return True


print(isEven(in1))
print(isEven(in2))
print(isEven(in3))
print(isEven(in4))
