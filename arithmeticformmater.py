def arithmetic_arrange(problems, show_answers = False):
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
        if operator[i] != "+" or operator[i] != "-":
            raise ValueError("Error: Operator must be '+' or '-'.")
        if firstOperand[i] is not int or secondOperand[i] is not int:
            raise ValueError("Error: Numbers must only contain digits.")
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

        if show_answers == True:
            fourthindividualline  = fourthindividualline + "  " + str((int(firstOperand[i]) + int(secondOperand[i])))   + "    "
        else:
            fourthindividualline = ""
        thirdindividualLine = thirdindividualLine + ("-" * (max(len(secondOperand[i]), len(firstOperand[i])) + 2)+ 4 * " ") 
        secondOperandLine = secondOperandLine + siL() + "    "
        return problems

    print(firstOperandLine)
    print(secondOperandLine)
    print(thirdindividualLine)
    print(fourthindividualline)

