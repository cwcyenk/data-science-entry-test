""" Solution for Question 1 """

def swap(x, y):
    """
    - Swap the values of x and y if they are numeric.
    - Else return -1 if either or both are not numeric. 
    """
    if isinstance(x, (int, float)) and isinstance(y, (int, float)) == True:
        print("The original values of x and y are {} and {}, respectively.".format(x, y))
        x, y = y, x
        print("After swapping, the values of x and y becomes {} and {}, respectively.".format(x, y))
    else:
        return -1
        
""" Test scenario 1 """
print("Test Scenario 1")
swap("Apple", 10)

print("\n")

""" Test scenario 2 """
print("Test Scenario 2")
swap(9, 17)
