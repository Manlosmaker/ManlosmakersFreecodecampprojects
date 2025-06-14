def arithmetic_arrange(calculations, answer = False):
    firstOperand = [] 
    secondOperand = []
    operator = ""
    for item in calculations:
        splitItem = item.split(" ")
        firstOperand.append(splitItem[0])
        secondOperand.append(splitItem[1])
        operator.append(splitItem[2])

calculations = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
arithmetic_arrange(calculations)