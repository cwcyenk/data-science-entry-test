""" Solution for Question 5 """

def check_divisibility(num, divisor):

    """
    - Check the divisiblity of a number (num) over a divisor using modulo
    - Return True if yes and False otherwise
    """
    return (True if num % divisor == 0 else False)


""" Test scenario 1 """
print("Test Scenario 1")
print(check_divisibility(10, 2))

print("\n")


""" Test scenario 2 """
print("Test Scenario 2")
print(check_divisibility(7, 3))