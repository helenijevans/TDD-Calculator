# TDD PROCESS
# first step - making a main method that takes in an input and then routes
# first step tests: ALL FAIL (6)
# - calling router function with equation and expecting a correct result (at the moment returning 0 for all)
# - calling router function with an invalid format and expect error message

# second step - adding and routing operator functions (which all return 0) and throwing exception in router
#               adding new tests to check correct flow from routing function
# second step tests: 1 PASS; 10 FAIL
# - calling router function with an invalid format and expect error message (PASSES)
# - calling operator functions and expecting a correct result (at the moment returning 0 for all)
# - flow tests replicate behaviour above and hence fail

# third step - changing operators logic to return correct calculation
# third step tests: 11 PASS
# - calling router function with an invalid format and expect error message (PASSES)
# - calling operator functions and expecting a correct result (PASS)
# - flow tests (PASS)

# fourth step - issue realised with dividing by 0
# fourth step tests: create new test case for dividing by 0
# 11 PASS, 1 FAIL (test_divide_by_zero)

# fifth step - add Exception Handling for that situation
# 12 TESTS PASS; DONE

## FINALISED CODE BELOW ##

import re


# main method for running program not for testing
def main():
    on = True
    print("*** Welcome to The Dapper Deluxe Calculator **")
    while on:
        print("\nTo exit write 'OFF'")
        user_input = input("Please enter your calculation in the form 'x ( + / - / * / / / **) y' ")
        if user_input == "OFF":
            on = False
            print("👋 Goodbye")
        else:
            print(router(user_input))


def router(equation):
    numbers = [int(s) for s in equation.split() if s.isdigit()]
    try:
        valid_check = numbers[1]
    except IndexError:
        return "Not in a valid format\nPlease try again\n"

    numbers_in_equation = r'[0-9]'
    operator = re.sub(numbers_in_equation, '', equation).strip()

    match operator:
        case '+':
            return add(numbers)
        case '-':
            return minus(numbers)
        case '*':
            return multiply(numbers)
        case '/':
            return divide(numbers)
        case '**':
            return power(numbers)


# operators take in an array of numbers
def add(numbers):
    return numbers[0] + numbers[1]


def minus(numbers):
    return numbers[0] - numbers[1]


def multiply(numbers):
    return numbers[0] * numbers[1]


def divide(numbers):
    try:
        return numbers[0] / numbers[1]
    except ZeroDivisionError:
        print("Can't divide a number by 0")
        print("Returning to main menu")
        main()


def power(numbers):
    return numbers[0] ** numbers[1]

# comment back in to run file
main()