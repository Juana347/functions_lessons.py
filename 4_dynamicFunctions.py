# Dynamic Functions Practice #1
# Create a function (all_positives) that returns True if all the values in a list are positive, and False if at least one of the values is negative. Create a list named numbers with positive and negative values.

# Don't call the function, you just need to define it.

list_numbers = [10, 25, -3, 42, 7]
def all_positives(list_numbers): 
    for num in list_numbers:
        if num < 0:
            return False
    return True
print(all_positives(list_numbers))





# Dynamic Functions Practice #2
# Create a function (sum_less) that adds the numbers of a list as long as they are greater than 0 and less than 1000, and returns the result of said sum. Create a numbers variable, storing a list of numbers so we can test it.

numbers = [150, 2000, 350, -50, 800, 999, 1001]
numbers2 = [10, 20, 30, 40, 50]
def sum_less(numbers):
    total = 0
    for num in numbers: 
        if 0 < num < 1000:
            total += num
    return total
print(sum_less(numbers))
print(sum_less(numbers2))



# Dynamic Functions Practice #3
# Create a function (count_even) that counts the number of even numbers that exist in a list (numbers), and returns the result of said count.

# numbers = [2, 3, 4, 7, 12, 14, 17, 21, 37]
# def count_even(numbers):

# print(count_even(numbers))
