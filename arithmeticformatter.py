
def arithmetic_arranger(problems, show_answers=False):
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
 
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
print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
