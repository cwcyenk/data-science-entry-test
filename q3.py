""" Solution for Question 3 """

def update_dictionary(dct, key, value):
    """
    - Updates the dictionary (dct) with a new key-value pair. 
    - Print the original value of the key, if exisits, and updates its value
    - Else just update its value
    - Return the updated dictionary. """
    if key not in dct:
        print("No key exists. Creating a new key-value pair")
        dct[key] = value
    else:
        print("The original value of {} is {}".format(key, dct[key]))
        dct[key] = value
        print("The new value of {} is {}".format(key, dct[key]))
    
    return dct

""" Test scenario 1 """
print("Test Scenario 1")
updated_dictionary = update_dictionary({}, "name", "Alice")
print("Updated dictionary: {}.".format(updated_dictionary))

print("\n")

""" Test scenario 2 """
print("Test Scenario 2")
updated_dictionary = update_dictionary({"age": 25}, "age", 26)
print("Updated dictionary: {}.".format(updated_dictionary))