def arithmetic_arrange(calculations, answer = False):
    firstOperand = [] 
    secondOperand = []
    operator = []
    firstOperandLine = ""
    secondOperandLine = ""
    thirdindividualLine = ""
    fourthindividualline = ""
    for item in calculations:
        splitItem = item.split(" ")
        firstOperand.append(splitItem[0])
        secondOperand.append(splitItem[2])
        operator.append(splitItem[1])
    
    for i in range(len(calculations)):
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

        if answer == True:
            fourthindividualline  = fourthindividualline + "  " + str((int(firstOperand[i]) + int(secondOperand[i])))   + "    "
        else:
            fourthindividualline = ""
        thirdindividualLine = thirdindividualLine + ("-" * (max(len(secondOperand[i]), len(firstOperand[i])) + 2)+ 4 * " ") 
        secondOperandLine = secondOperandLine + siL() + "    "

    print(firstOperandLine)
    print(secondOperandLine)
    print(thirdindividualLine)
    print(fourthindividualline)


calculations = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
arithmetic_arrange(calculations, True)