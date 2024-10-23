import re
from django.shortcuts import render
from .Calculator import (
    cube_root, factorial, calculate_percentage, log, power_of_x, square, cube,
    power_of_2, exponential, sine, cosine, tangent, cotangent, secant, cosecant
)

def parse_custom_operator(expression, operator):
    """
    Parses an expression with a custom operator (%, ^, √) and returns the split parts.
    """
    pattern = rf'(\d+(\.\d+)?\s*{re.escape(operator)}\s*\d+(\.\d+)?)'
    match = re.search(pattern, expression)
    if match:
        return [x.strip() for x in expression.split(operator)]
    return []

def index(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        display = request.POST.get('display', '')

        action = str(action) if action else ''
        display = str(display) if display else ''

        if action == 'AC':
            display = ''
        elif action == 'DEL':
            display = display[:-1]
        elif action == '𝛑':
            display += '3.14159265359'
        elif action.isdigit() or action in ['.', '+', '-', '*', '/', '(', ')']:
            display += action
        elif action == '=':
            try:
                display = str(eval(display, {"__builtins__": None}, {}))
            except Exception as e:
                display = f'Error: {e}'
        else:
            display += action


        if 'cube_root' in display:
            try:
                number = display.replace('cube_root', '').strip()
                display = str(cube_root(float(number)))
            except (ValueError, IndexError) as e:
                display = f'Error: {e}'

        elif 'factorial' in display:
            try:
                number = display.replace('factorial', '').strip()
                display = str(factorial(int(number)))
            except (ValueError, IndexError) as e:
                display = f'Error: {e}'

        elif 'square' in display:
            try:
                number = display.replace('square', '').strip()
                display = str(square(float(number)))
            except (ValueError, IndexError) as e:
                display = f'Error: {e}'

        elif 'cube' in display:
            try:
                number = display.replace('cube', '').strip()
                display = str(cube(float(number)))
            except (ValueError, IndexError) as e:
                display = f'Error: {e}'

        elif 'sine' in display:
            try:
                number = display.replace('sine','').strip()
                display = str(sine(float(number)))
            except (ValueError,IndexError) as e:
                display = f'Error: {e}' 

        elif 'cosine' in display:
            try:
                number = display.replace('cosine','').strip()
                display = str(cosine(float(number)))
            except (ValueError,IndexError) as e:
                display = f'Error: {e}'

        elif 'tangent' in display:
            try:
                number = display.replace('tangent','').strip()
                display = str(tangent(float(number)))
            except (ValueError,IndexError) as e:
                display = f'Error: {e}' 

        elif 'cotangent' in display:
            try:
                number = display.replace('cotangent','').strip()
                display = str(cotangent(float(number)))
            except (ValueError,IndexError) as e:
                display = f'Error: {e}' 

        elif 'secant' in display:
            try:
                number = display.replace('secant','').strip()
                display = str(secant(float(number)))
            except (ValueError,IndexError) as e:
                display = f'Error: {e}'

        elif 'cosecant' in display:
            try:
                number = display.replace('cosecant','').strip()
                display = str(cosecant(float(number)))
            except (ValueError,IndexError) as e:
                display = f'Error: {e}' 

        elif 'power_of_2' in display:
            try:
                number = display.replace('power_of_2','').strip()
                display = str(power_of_2(float(number)))
            except (ValueError,IndexError) as e:
                display = f'Error: {e}'    

        elif 'exponential' in display:
            try:
                number = display.replace('exponential','').strip()
                display = str(exponential(number))
            except (ValueError,IndexError) as e:
                display = f'Error: {e}'                                              

        elif '^' in display:
            try:
                numbers = parse_custom_operator(display, '^')
                if len(numbers) == 2:
                    x = float(numbers[0])
                    y = float(numbers[1])
                    display = str(power_of_x(x, y))
            except (ValueError, IndexError) as e:
                display = f'Error: {e}'

        elif '%' in display:
            try:
                numbers = parse_custom_operator(display, '%')
                if len(numbers) == 2:
                    score = float(numbers[0])
                    total = float(numbers[1])
                    display = str(calculate_percentage(score, total))
            except (ValueError, IndexError) as e:
                display = f'Error: {e}'

        elif '√' in display:
            try:
                number = display.replace('√', '').strip()
                display = str(power_of_x(float(number)))
            except (ValueError, IndexError) as e:
                display = f'Error: {e}'

        elif 'log' in display:
            try:
                numbers = parse_custom_operator(display, 'log')
                if len(numbers) == 2:
                    base = float(numbers[0])
                    value = float(numbers[1])
                    display = str(log(base, value))
                else:
                    display = 'Error: Invalid input for logarithm'
            except (ValueError, IndexError) as e:
                display = f'Error: {e}'

        return render(request, 'index.html', {'display': display})

    return render(request, 'index.html', {'display': ''})
