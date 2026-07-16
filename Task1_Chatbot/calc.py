def calculate(expression):
    try:
        if "+" in expression:
            parts = expression.split("+")
            a = float(parts[0])
            b = float(parts[1])
            result = a + b

        elif "-" in expression:
            parts = expression.split("-")
            a = float(parts[0])
            b = float(parts[1])
            result = a - b

        elif "**" in expression:
            parts = expression.split("**")
            a = float(parts[0])
            b = float(parts[1])
            result = a ** b

        elif "*" in expression:
            parts = expression.split("*")
            a = float(parts[0])
            b = float(parts[1])
            result = a * b

        elif "/" in expression:
            parts = expression.split("/")
            a = float(parts[0])
            b = float(parts[1])
            result = a / b

        elif "%" in expression:
            parts = expression.split("%")
            a = float(parts[0])
            b = float(parts[1])
            result = a % b

        else:
            print("Bot: Invalid expression!")
            return

        # Print result
        if result.is_integer():
            print(f"Bot: Result = {int(result)}")
        else:
            print(f"Bot: Result = {result}")

    except ValueError:
        print("Bot: Please enter valid numbers.")

    except ZeroDivisionError:
        print("Bot: Cannot divide by zero.")