#!/usr/bin/env python3
"""
A Python script that demonstrates various programming patterns.
This is the fixed version of the previously buggy script.
"""

import sys
import random
import threading
# Removed the non-existent import

# Fixed: Added missing colon
def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    total = sum(numbers)
    return total / len(numbers)

# Fixed: Proper indentation
def print_message(msg):
    print(msg)

# Fixed: Removed use of undefined variable
def use_defined_variable():
    defined_var = 5
    result = defined_var + 10
    return result

# Fixed: Convert int to string for concatenation
def concatenate_correctly():
    age = 25
    message = "Your age is: " + str(age)
    return message

# Fixed: Added check for division by zero
def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Fixed: Access valid index
def get_item_from_list():
    my_list = [1, 2, 3]
    if len(my_list) > 2:
        return my_list[2]
    return None

# Fixed: Added increment to avoid infinite loop
def count_to_ten():
    i = 0
    while i < 10:
        print(i)
        i += 1  # Fixed: increment i

# Fixed: Use correct method for dict
def use_dict_correctly():
    my_dict = {"name": "John"}
    my_dict["value"] = "added"  # Use dict assignment instead of append
    return my_dict

# Fixed: Added return statement
def get_user_info():
    user = {"name": "Alice", "age": 30}
    return user  # Fixed: return the dict

# Fixed: Properly close file using context manager
def read_file_safely(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
        return content
    except FileNotFoundError:
        return None

# Fixed: Don't use mutable default argument
def append_to_list(item, target=None):
    if target is None:
        target = []
    target.append(item)
    return target

# Fixed: Use 'is' for None comparison
def check_none(value):
    if value is None:  # Fixed: use 'is None'
        return True
    return False

# Fixed: Don't shadow built-ins
def create_list():
    my_list = [1, 2, 3]  # Fixed: renamed to avoid shadowing
    return my_list

# Fixed: Use parameterized queries (example using placeholder)
def safe_query(user_input):
    # In real code, use proper parameterized queries with your DB library
    query = "SELECT * FROM users WHERE name = ?"
    # Return query and parameters separately
    return query, (user_input,)

# Fixed: Thread-safe counter using lock
counter = 0
counter_lock = threading.Lock()

def increment_counter():
    global counter
    with counter_lock:
        counter += 1

# Fixed: Weak references can help with circular references
import weakref

class Node:
    def __init__(self, value):
        self.value = value
        self._parent = None  # Will use weak reference
        self.children = []
    
    @property
    def parent(self):
        return self._parent() if self._parent else None
    
    @parent.setter
    def parent(self, parent):
        self._parent = weakref.ref(parent) if parent else None
    
    def add_child(self, child):
        self.children.append(child)
        child.parent = self

# Fixed main function
def main():
    # Calculate average safely
    avg = calculate_average([1, 2, 3, 4, 5])
    print(f"Average: {avg}")
    
    # Print message
    print_message("Hello, World!")
    
    # Safe division
    try:
        result = divide_numbers(10, 2)
        print(f"Division result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    
    # Correct string concatenation
    message = concatenate_correctly()
    print(message)
    
    # Use defined variable
    value = use_defined_variable()
    print(f"Calculated value: {value}")
    
    # Safe list access
    item = get_item_from_list()
    print(f"List item: {item}")
    
    # Get user info with proper return
    info = get_user_info()
    print(f"User info: {info}")
    
    # Fixed comparison
    x = 5
    if x == 5:  # Fixed: use == for comparison
        print("x is 5")
    
    # Demonstrate other fixed functions
    print("\nDemonstrating other fixes:")
    
    # Count without infinite loop
    print("Counting to 3:")
    i = 0
    while i < 3:
        print(i)
        i += 1
    
    # Use dict correctly
    my_dict = use_dict_correctly()
    print(f"Updated dict: {my_dict}")
    
    # Check None properly
    print(f"None check: {check_none(None)}")
    
    # Create list without shadowing
    my_list = create_list()
    print(f"Created list: {my_list}")
    
    # Safe query example
    query, params = safe_query("Alice")
    print(f"Safe query: {query} with params: {params}")

if __name__ == "__main__":
    main()