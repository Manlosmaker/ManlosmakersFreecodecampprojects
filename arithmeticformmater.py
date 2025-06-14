def arithmetic_arrange(calculations, answer = False):
    firstOperand = [] 
    secondOperand = []
    operator = []
    firstOperandLine = ""
    secondOperandLine = ""

    for item in calculations:
        splitItem = item.split(" ")
        firstOperand.append(splitItem[0])
        secondOperand.append(splitItem[2])
        operator.append(splitItem[1])
    
    for i in range(len(calculations)):
        individialLine = max(len(firstOperand[i]), len(secondOperand[i]) + 1) * " " + firstOperand[i]
        firstOperandLine = firstOperandLine + individialLine + "    "
        secondindividualLine = operator[i] + (len(firstOperand[i]) * " ") + secondOperand[i]
        secondOperandLine = secondOperandLine + secondindividualLine + "    "
    print(firstOperandLine)
    print(secondOperandLine)

calculations = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
arithmetic_arrange(calculations)