""" Solution for Question 2"""

def find_and_replace(lst, find_val, replace_val):
    """
    - Search for find_val in the lst and replace with replace_val.
    """

    return [replace_val if x == find_val else x for x in lst]
    
""" Test scenario 1 """
print("Test Scenario 1")
modified_list = find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
print(modified_list)

print("\n")

""" Test scenario 2 """
print("Test Scenario 2")
modified_list = find_and_replace(["apple", "banana", "apple"], "apple", "orange")
print(modified_list)