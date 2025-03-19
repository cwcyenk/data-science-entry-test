""" Solution for Question 4 """

def string_reverse(s):
    """
    - Reverses the string s and return the reversed string 
    """

    return (s[::-1])

""" Test scenario 1 """
print("Test Scenario 1")
reversed_string = string_reverse("Hello World")
print(reversed_string)

print("\n")

""" Test scenario 2 """
print("Test Scenario 2")
reversed_string = string_reverse("Python")
print(reversed_string)