import re

def arithmetic_arranger(problems, display_results=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    mat = [[], [], []]  # Apenas três elementos para os problemas originais
    results = []  # Lista para armazenar os resultados

    for problem in problems:
        # Usar uma expressão regular para separar os componentes do problema
        componentes = re.split(r'\s*([\+\-])\s*', problem)
        if len(componentes) != 3:
            return "Error: Operator must be '+' or '-'."

        num1, operador, num2 = componentes
        if operador not in "+-":
            return "Error: Operator must be '+' or '-'."
        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."

        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        comprimento = max(len(num1), len(num2)) + 2

        mat[0].append(num1.rjust(comprimento))
        mat[1].append(operador + ' ' + num2.rjust(comprimento - 2))
        mat[2].append('-' * comprimento)

        if operador == "+":
            num3 = str(int(num1) + int(num2))
        elif operador == "-":
            num3 = str(int(num1) - int(num2))
        else:
            return "Error: Unsupported operator."

        results.append(num3.rjust(comprimento))  # Adicionar o resultado à lista de resultados

    arranged_problems = '\n'.join(['    '.join(mat[i]) for i in range(3)])

    if display_results:
        arranged_problems += '\n' + '    '.join(results)  # Adicionar os resultados ao final

    return arranged_problems
