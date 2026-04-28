'''
Students in primary school often arrange arithmetic problems vertically to make them easier to solve. For example, "235 + 52" becomes:

  235
+  52
-----
Finish the arithmetic_arranger function that receives a list of strings which are arithmetic problems, and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.
'''

def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dashes = []
    answers = []

    for problem in problems:
        item = problem.split()
        num1 = item[0]
        operador = item[1]
        num2 = item[2]

        # Correção da mensagem de erro (adicionado o ponto final)
        if operador != '+' and operador != '-':
            return "Error: Operator must be '+' or '-'."

        if not num1.isdigit() or not num2.isdigit():
            return 'Error: Numbers must only contain digits.'

        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        length = max(len(num1), len(num2)) + 2

        first_line.append(num1.rjust(length))
        second_line.append(operador + num2.rjust(length - 1))
        dashes.append("-" * length)

        if show_answers:
            if operador == '+':
                res = str(int(num1) + int(num2))
            else:
                res = str(int(num1) - int(num2))
            answers.append(res.rjust(length))

    final_first = "    ".join(first_line)
    final_second = "    ".join(second_line)
    final_dashes = "    ".join(dashes)

    if show_answers:
        final_answers = "    ".join(answers)
        return f"{final_first}\n{final_second}\n{final_dashes}\n{final_answers}"
    
    return f"{final_first}\n{final_second}\n{final_dashes}"