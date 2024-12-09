def function_with_uncommon_error_solution(x):
    try:
        if isinstance(x,str):
            raise TypeError("Cannot divide by a string")
        result = 10 / x
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except TypeError as e:
        print(f"Error: {e}")
        return None

# Input validation and improved handling of TypeError
result = function_with_uncommon_error_solution(5)
print(result)  # Output: 2.0

result = function_with_uncommon_error_solution("abc")
print(result) # Output: Error: Cannot divide by a string
None
result = function_with_uncommon_error_solution(0)
print(result) # Output: Error: Cannot divide by zero.
None