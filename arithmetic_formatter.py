# Created an arithmetic function that receives strings which are arithmetic problems, and returns the problems arranged vertically and side-by-side.


def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = {"top": "", "bottom": "", "lines": "", "answers": ""}

    for problem in problems:
        operand1, operator, operand2 = problem.split()

        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        max_length = max(len(operand1), len(operand2))

        arranged_problems["top"] += operand1.rjust(max_length + 2) + "    "
        arranged_problems["bottom"] += (
            operator + " " + operand2.rjust(max_length) + "    "
        )
        arranged_problems["lines"] += "-" * (max_length + 2) + "    "

        if show_answers:
            answer = str(eval(problem)).rjust(max_length + 2)
            arranged_problems["answers"] += answer + "    "

    arranged_format = (
        arranged_problems["top"].rstrip()
        + "\n"
        + arranged_problems["bottom"].rstrip()
        + "\n"
        + arranged_problems["lines"].rstrip()
    )

    if show_answers:
        arranged_format += "\n" + arranged_problems["answers"].rstrip()

    return arranged_format


print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
