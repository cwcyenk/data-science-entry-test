""" Solution for Question 6 """

def find_first_negative(lst):
    """
    - Finds and returns the first negative number in a list.
    - If no negative number found, return "No negatives".
    """

    index = 0
    while index < len(lst):
        if lst[index] < 0:
            return (lst[index])
        index += 1

    return "No negatives"


""" Test scenario 1 """
print("Test Scenario 1")
print(find_first_negative([3, 5, -1, 7, -2, 8]))

print("\n")


""" Test scenario 2 """
print("Test Scenario 2")
print(find_first_negative([2, 10, 7, 0]))