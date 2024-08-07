# Write a Python program to calculate the sum of values in a dictionary.

# Create a dictionary with some key-value pairs
my_dict = {
    'item1': 10,
    'item2': 25,
    'item3': 40,
    'item4': 15
}

# Function to calculate the sum of values in the dictionary


def sum_of_values(dictionary):
    total = 0
    # Iterate through the values in the dictionary and add them to the total
    for value in dictionary.values():
        total += value
    return total


# Example usage
total_sum = sum_of_values(my_dict)
print(f"The sum of the values in the dictionary is: {total_sum}")
