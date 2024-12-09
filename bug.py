def function_with_uncommon_error(x):
    try:
        result = 10 / x
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except TypeError:
        print("Error: Unsupported operand type(s) for /.")
        return None

# Uncommon error:  Passing a string to a mathematical function
result = function_with_uncommon_error("abc")
print(result) # Output: Error: Unsupported operand type(s) for /.
None