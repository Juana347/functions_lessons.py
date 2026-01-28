def tea_order(customer_name, tea_type, **kwargs):
    print(customer_name, "ordered a", tea_type, "tea")
    for key, value in kwargs.items():
        print(" - Add", key, ":", value)
   
tea_order("Alice", "chamomile")
tea_order("Bob", "black", milk="oat")
tea_order("Tony", "black", milk="oat", sweetner="honey")

# Indefinite Arguments (*args) Practice #1
# Create a function called sum_squares that takes any number of numeric arguments, and returns the sum of their values squared.

# For example for the arguments sum_squares(1,2,3) it should return 14 (1+4+9).
def sum_squares(*args):
    sum = 0 #Initialize sum to 0 
    for num in args:   #Iterate throug each argument
        sum += num **2 #Squre the number and add it to sum
        # 1st time through: sum = 0 + 4 = 4
        # 2nd time through: sum = 4 + 5 + 9
    return sum 
print(sum_squares(4, 5, 6, 7, 7, 7, 8, 9, 9, 9))  # Returns 531


# Indefinite Arguments (*args) Practice #2
# Create a function called absolute_sum, which takes any number of arguments, and returns the sum of their absolute values (that is, it takes the non-negative values and adds them together, 
# in other words, considers them all - negative and positive - as positive).
def absolute_sum(*args):
    sum = 0  #Initialize sum to 0
    for num in args:  #Iterate through each argument
        sum += abs(num) #Add the absolute value of the number to the sum
    return sum
list_of_numbers = [10, 5, -3, 7, -2, 6, 7, -8, 9]  
print(absolute_sum(*list_of_numbers)) # Unpack the list and pass as arguments 


# Indefinite Arguments (*args) Practice #3
# Create a function called personal_numbers that receives, as its first argument, a name, and then an indefinite number of values.

# The function should return the following message:

# "{name}, the sum of your numbers is {sum_numbers}"
def personal_numbers(name, *args):
    sum_numbers = 0 
    for num in args: #Iterate thorugh each argument
        sum_numbers += num # Add the number to sum_numbers
    return f"{name}, the sum of your numbers is {sum_numbers}"

print(personal_numbers("Alice", 3, 7, 2, 8)) # returns 20