import operator


def arithmetic_arranger(problems, answer=False):
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    # Function only accept max 5 problem
    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        # Split operators and operand
        problem = problem.split()
        problem_operand1 = problem[0]
        problem_operand2 = problem[2]
        problem_operator = None

        # Function only accept max 4 digit number
        if len(problem_operand1) > 4 or len(problem_operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Checks for alpha characters in number
        if not problem_operand1.isnumeric() or not problem_operand2.isnumeric():
            return "Error: Numbers must only contain digits."

        # Find operator and answer
        match problem[1]:
            case '+':
                problem_operator = operator.add
            case '-':
                problem_operator = operator.sub
            case _:
                return "Error: Operator must be '+' or '-'."
        problem_answer = problem_operator(
            int(problem_operand1), int(problem_operand2))

        # Lines length
        problem_operand1_length = len(problem_operand1)
        problem_operand2_length = len(problem_operand2)
        problem_answer_length = len(str(problem_answer))
        max_line_size = max(problem_operand1_length + 2, problem_operand2_length + 2,
                            problem_answer_length + 1)

        # Line Constructor
        line1 += f"{' ' * (max_line_size - problem_operand1_length - 1)} {problem_operand1}    "
        line2 += f"{problem[1]}{' ' * (max_line_size - problem_operand2_length - 2)} {problem_operand2}    "
        line3 += f"{'-' * max_line_size}    "
        line4 += f"{' ' * (max_line_size - problem_answer_length - 1)} {problem_operator(int(problem_operand1), int(problem_operand2))}    "

    # When answer is required
    if answer:
        return f"{line1.rstrip()}\n{line2.rstrip()}\n{line3.rstrip()}\n{line4.rstrip()}"

    # When answer is not required
    return f"{line1.rstrip()}\n{line2.rstrip()}\n{line3.rstrip()}"


if __name__ == "__main__":
    print(arithmetic_arranger(
        ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], 1))
