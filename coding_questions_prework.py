# Question 1: Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
    '''Prints a simple greeting to the input. '''
    print(f'Hello, {user_name.title()}!')

name = input('What is your name? ')

hello_name(name)

# Question 2: Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    '''Prints a list off odd numbers between 1-100'''
    num_list = list(range(1,100,2))
    print(num_list)

first_odds()

# Question 3: Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
    '''Returns the max number in a given list'''
    return max(a_list)

random_list = [5,6,4,21,22,65,23,3,52]
print(max_num_in_list(random_list))

# Question 4: Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible
# by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    '''Returns if a year is a leap year in boolean (true/false)'''
    if a_year % 4 != 0:
        return False
    elif a_year % 400 == 0:
        return True
    else:
        return False

print(is_leap_year(2000))


# Question 5: Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are 
# not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    '''Returns if a given list contains consecutive numbers.'''
    if sorted(a_list) == list(range(min(a_list), max(a_list)+1)):
        return True
    else:
        return False

b_list = [7,3,4,5,6,2]
print(is_consecutive(b_list))







    


