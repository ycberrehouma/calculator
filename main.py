def my_function():
    print('Welcome to The Best Calculator Written in Python 3\n')

    #value1 = value2 = total =0
    value1 = int(input('enter the first value to be calculated\n'))
    value2 = int(input('enter the second value to be calculated\n'))

    operator = input('for + press +\n'
                     'for - press -\n'
                     'for * press *\n'
                     'for / press / \n')

    if operator == '+':
        total = value1 + value2

    elif operator == '-':
        total = value1 - value2

    elif operator == '*':
        total = value1 * value2

    elif operator == '/':
        total = value1 / value2

    operators = ['+', '-', '/', '*']
    if operator not in operators:
        print('You entered an undefined operator, try again ')

    else:
        print('the total for ', value1, operator, value2, ' is equal to', total, '\n')
        option = input('press r to retry \n')

        if option == 'r':
            my_function()


        else:
            print('Thank You! Good Bye')


my_function()