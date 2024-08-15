def arithmetic_arranger(problems, show_answers = False):
    # Check if there are more than 5 problems
    if len(problems) > 5:
        return 'Error: Too many problems.'
   
    for problem in problems:
        char_iterator = 0

        # Check problems operator, only (+) and (-) are allowed
        if '*' in problem or '/' in problem:
            return "Error: Operator must be '+' or '-'."

        for char in problem.replace(' ', ''):
            # Check if there are non-digits inside the problems
            if not char.isdigit() and char not in ['+', '-']:
                return 'Error: Numbers must only contain digits.'
            
            # Check max digit lenght(4)
            if char in ['+', '-']:
                char_iterator = 0
            else: 
                char_iterator += 1
                if char_iterator > 4:
                    return 'Error: Numbers cannot be more than four digits.'
    
    top_row = ''
    bottom_row = ''
    separator = ''
    answers_row = ''

    # Checks if the value given is not the last one in the current row and adds spaces between
    def is_last_value_in_row(i):
        if i != len(problems) - 1:
            return ' ' * 4
        else:
            return ''

    # Evalute problem solutions and formatting
    for i, problem in enumerate(problems):
        operation = problem.split()
        firstNum = int(operation[0])
        secondNum = int(operation[2])
        operator = operation[1]
        space = max(len(str(firstNum)), len(str(secondNum))) + 2

        # Add numbers
        if operator == '+':
            result = firstNum + secondNum
            # Add the result to the answers_row
            answers_row += str(result).rjust(space) + is_last_value_in_row(i)
        # Subtract numbers
        else:
            result = firstNum - secondNum
            # Add the result to the answers_row
            answers_row += str(result).rjust(space) + is_last_value_in_row(i)

        # Add top numbers
        top_row += str(firstNum).rjust(space) + is_last_value_in_row(i)
        # Add bottom numbers
        bottom_row += operator + str(secondNum).rjust(space - 1) + is_last_value_in_row(i)
        # Add separators
        separator += '-' * space + is_last_value_in_row(i)
  

    if show_answers:
        # Show the formatted string with the answers if show_answers is True
        return f"{top_row}\n{bottom_row}\n{separator}\n{answers_row}"
    else:
        # Show the formatted string without the answers if show_answers is False
        return f"{top_row}\n{bottom_row}\n{separator}"
     

print(f'\n{arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49", "55 - 5"], True)}')