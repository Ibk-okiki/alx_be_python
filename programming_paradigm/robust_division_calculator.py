# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Convert to float first
        num = float(numerator)
        denom = float(denominator)

        # Attempt division
        result = num / denom
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
      
