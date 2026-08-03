class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+": lambda b, a: a + b,
            "-": lambda b, a: b - a,
            "*": lambda b, a: a * b,
            "/": lambda b, a: int(b / a),
        }
        stack = []
        for token in tokens:
            if token in operators:
                a, b = stack.pop(), stack.pop()
                stack.append(operators[token](b, a))
            else:
                stack.append(int(token))
        return stack.pop()