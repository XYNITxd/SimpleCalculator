float_int = str(input("Decimal or whole? "))
answers = ["whole", "decimal"]
if float_int.lower() in answers:
    if float_int.lower() == str("decimal"):
        num1 = float(input("First number: "))
        op = input("Operator: ")
        num2 = float(input("Second number: "))
    elif float_int.lower() == str("whole"):
        try:
            num1 = int(input("First number: "))
            op = input("Operator: ")
            num2 = int(input("Second number: "))
        except ValueError:
            print("Please enter a whole number instead of a decimal")
            op = "stop"
else:
    print("Please respond with either 'decimal' or 'whole'")
    op = "stop"

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    try:
        print(num1 / num2)
    except ZeroDivisionError:
        print("You can't divide by zero!")
elif op == "%":
    print(num1 % num2)
elif op == "**":
    print(num1 ** num2)
elif op == "//":
    try:
        print(num1 // num2)
    except ZeroDivisionError:
        print("You can't divide by zero!")
elif op == "stop":
    pass
else:
    print(f"{op} is not a valid operator!")
