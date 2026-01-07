def history_save(equation, result):
    file = open("history.txt", "a")
    file.write(equation + " = " + str(result) + "\n")
    file.close()


def calculator(userinput):
    parts = userinput.split()

    if len(parts) != 3:
        print("Invalid format! Use: number operator number")
        return

    try:
        num1 = float(parts[0])
        op = parts[1]
        num2 = float(parts[2])
    except ValueError:
        print("Please enter valid numbers")
        return

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Cannot divide by zero")
            return
        result = num1 / num2
    else:
        print("Invalid operator")
        return

    print("Result:", result)
    history_save(userinput, result)


while True:
    userinput = input(
        "Enter calculation (+ - * /) or type history / exit: "
    ).strip().lower()

    if userinput == "history":
        file = open("history.txt", "r")
        print(file.read())
        file.close()

    elif userinput == "exit":
        print("Goodbye 👋")
        break

    else:
        calculator(userinput)
    




     










 

