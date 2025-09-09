#!/usr/bin/env python3
"""
Test file with intentional bugs to demonstrate bug detection.
"""

# Bug: Division by zero
def calculate_ratio(a, b):
    return a / 0  # This will always fail

# Bug: Mutable default argument
def append_to_list(item, my_list=[]):
    my_list.append(item)
    return my_list

# Bug: Comparison with None using ==
def check_value(val):
    if val == None:  # Should use 'is None'
        return "Value is None"
    return "Value is not None"

# Bug: Bare except clause
def risky_operation():
    try:
        undefined_var + 10  # Bug: undefined variable
    except:  # Bad: bare except
        pass

# Bug: Missing return statement
def get_sum(a, b):
    result = a + b
    # Forgot to return result

# Debug print left in code
def process_data(data):
    print("DEBUG: Processing data:", data)  # Should remove debug prints
    return data * 2

# Hardcoded secret
API_KEY = "sk-1234567890abcdef"  # Security issue!
password = "admin123"  # Another security issue!

# TODO: Fix this function
def incomplete_function():
    # FIXME: This needs implementation
    pass

# Test the functions
if __name__ == "__main__":
    # This will demonstrate the bugs
    print("Testing buggy code...")
    
    # Will raise ZeroDivisionError
    try:
        print(calculate_ratio(10, 5))
    except ZeroDivisionError:
        print("Caught division by zero!")
    
    # Demonstrates mutable default issue
    list1 = append_to_list("item1")
    list2 = append_to_list("item2")
    print(f"list2 unexpectedly contains: {list2}")  # Will show ['item1', 'item2']
    
    # Test None comparison
    print(check_value(None))
    
    # Missing return
    result = get_sum(5, 3)
    print(f"Sum result: {result}")  # Will print None