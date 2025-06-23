<<<<<<< HEAD
def arithmetic_arranger(problems, show_answers=False):
=======
def arithmetic_arranger(problems, show_answers=True):
>>>>>>> a0f961383ecd0086dea27f3262d42c86ef9ba958
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
<<<<<<< HEAD
 
=======

>>>>>>> a0f961383ecd0086dea27f3262d42c86ef9ba958
    if len(problems) > 5:
        return "Error: Too many problems."
    
    for item in problems:
        #splitting items
        splitItem = item.split(" ")
        num1 = splitItem[0]
        operand = splitItem[1]
        num2 = splitItem[2]
        if num1.isdigit() != True or num2.isdigit() != True:
            return 'Error: Numbers must only contain digits.'
        maxLen = max(len(num1),len(num2))

        #error handling
        if operand != "+" and operand != "-":
            return "Error: Operator must be '+' or '-'."

        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        #making the lines
        line1 = line1 + f"{int(num1):>{maxLen + 2}}    " 
        line2 = line2 + f"{operand} {num2:>{maxLen}}    "
        line3 = line3 + "-" * (maxLen + 2) + "    "  
        #checking if show answers is true
        if show_answers and operand == "+":

            line4 = line4 + f"{(int(num1) + int(num2)):>{maxLen+2}}    "
        elif show_answers and operand == "-":
            line4 = line4 + f"{(int(num1) - int(num2)):>{maxLen+2}}    "
    lines = [
        line1.rstrip(),
        line2.rstrip(),
        line3.rstrip(),
    ]
    if show_answers:
        lines.append(line4.rstrip())

    problems = "\n".join(lines)
    return problems
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
