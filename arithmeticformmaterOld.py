def arithmetic_arranger(problems, show_answers=False):
    firstOperand = [] 
    secondOperand = []
    operator = []
    firstOperandLine = ""
    secondOperandLine = ""
    thirdindividualLine = ""
    fourthindividualline = ""
    for item in problems:
        splitItem = item.split(" ")
        firstOperand.append(splitItem[0])
        secondOperand.append(splitItem[2])
        operator.append(splitItem[1])
    if len(firstOperand) > 5:
        raise ValueError("Error Too many problems.")
    
    for i in range(len(problems)):
        if operator[i] == "+" and operator[i] == "-":
            raise ValueError("Error: Operator must be '+' or '-'.")
        if len(firstOperand[i]) > 4 or len(secondOperand[i]) > 4:
            raise ValueError("Error: Numbers cannot be more than four digits.")
        def miL(): 
            if len(firstOperand[i]) >= len(secondOperand[i]):
                individialLine = 2 * " " + firstOperand[i]
            else:
                individialLine = (len(secondOperand[i]) - len(firstOperand[i]) + 2) * " " + firstOperand[i]
            return individialLine
        firstOperandLine = firstOperandLine + miL() + "    "
        def siL():
            if len(secondOperand[i]) >= len(firstOperand[i]): 
                secondindividualLine = operator[i] + " " + secondOperand[i]
            elif len(firstOperand[i]) == 3: 
                secondindividualLine = operator[i] + 2 * " " + secondOperand[i]
            else: 
                secondindividualLine = operator[i] + (len(firstOperand[i])) * " " + secondOperand[i]
            return secondindividualLine

        if show_answers == True and len(str(int(firstOperand[i]) + int(secondOperand[i]))) == max(len(firstOperand[i]),len(secondOperand[i])):
            fourthindividualline = fourthindividualline + "  " + str((int(firstOperand[i]) + int(secondOperand[i])))   + "    "
        elif show_answers == True and len(str(int(firstOperand[i]) + int(secondOperand[i]))) != max(len(firstOperand[i]),len(secondOperand[i])):
            fourthindividualline = fourthindividualline + " " + str((int(firstOperand[i]) + int(secondOperand[i])))   + "    "
        else:
            fourthindividualline = ""
        thirdindividualLine = thirdindividualLine + ("-" * (max(len(secondOperand[i]), len(firstOperand[i])) + 2)+ 4 * " ") 
        secondOperandLine = secondOperandLine + siL() + "    "
    (firstOperandLine)
#    if fourthindividualline != "":
#        print(fourthindividualline)
#    else:
#        pass
    problems = f"{firstOperandLine}\n{secondOperandLine}\n{thirdindividualLine}"
# add \n{fourthindividualline} later
    return problems




print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')