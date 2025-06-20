def arithmetic_arranger(problems, show_answers=False):
    for item in problems:
        #splitting items
        splitItem = item.split(" ")
        num1 = int(splitItem[0])
        operand = splitItem[1]
        num2 = int(splitItem[2])
        maxLen = max(len(str(num1)),len(str(num2)))

        #line 1
        line1 = maxLen - len(str(num1))
        if maxLen - len(str(num1)) == 0:
            line1 = f"{num1:>maxLen}"
        print(line1)

    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')