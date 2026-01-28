# Return Practice #1
# Create a function called power that takes two numeric values as arguments. It must return the number that results from solving a power, using the first number as the base, and the second as the exponent
def power(base, exponent): 
    return base ** exponent
power(3, 4)
print(power)





# Return Practice #2
# Create a function called usd_to_eur that takes a numeric value (an amount in US dollars) as its only parameter, and returns the equivalent amount in euros as a result. For the purposes of this example, we will take the conversion 1 USD = 0.90 EUR.

# Create a variable called dollars and store any amount in it. Then, pass it to your function and evaluate its result.

# Hint: to perform the conversion, the function internally must multiply this value in dollars by 0.90 to obtain the equivalent amount in euros.
def usd_to_eur(amount):
    return amount * 0.90
usd_to_eur(100)
print(usd_to_eur)

# Return Practice #3
# Create a function called reverse_word that takes the characters of a given word as an argument, reverses the order of their characters, and returns them that way and in uppercase.

# For example, if we pass it the word "Python", it should return: "NOHTYP"

# Also, you must create a variable called word, which contains any string, to pass it as an argument to the created function.

# Hint: inside the created function, you should use string methods already seen.
def reverse_word(word):
    word = word.upper()
    word = word[::-1]
    return word
print(reverse_word("Word"))
