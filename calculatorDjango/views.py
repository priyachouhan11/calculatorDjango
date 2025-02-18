# views.py
from django.shortcuts import render
from .Calculator import (
    abs_fun, cube_root, factorial, calculate_percentage, find_hcf, log, power_of_x, square, cube,
    power_of_2, exponential, sine, cosine, tangent, cotangent, secant, cosecant, degrees_to_radians
)

def index(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        display = request.POST.get('display', '')

        action = str(action) if action else ''
        display = str(display) if display else ''

        if action == 'AC':
            display = ''
        elif action == '𝛑':
            display = '3.14159265359'    
        elif action == '=':
            try:
                display = str(eval(display, {"__builtins__": None}, {}))
            except Exception as e:
                display = f'Error: {e}'
        else:
            display += action

        
        # if 'e^' in display:
            

        if 'cube_root' in display:
            try:
                number = display.replace('cube_root', '').strip()
                display = str(cube_root(eval(number)))
            except ValueError as e:
                display = f'Error: {e}'

        elif 'factorial' in display:
            try:
                number = display.replace('factorial', '').strip()
                display = str(factorial(int(number)))
            except (ValueError) as e:
                display = f'Error: {e}'

        elif 'square' in display:
            try:
                number = display.replace('square', '').strip()
                display = str(square(int(number)))
            except (ValueError) as e:
                display = f'Error: {e}' 

        elif 'power_of_2' in display:
            try:
                number = display.replace('power_of_2', '').strip()
                display = str(power_of_2(int(number)))
            except (ValueError) as e:
                display = f'Error: {e}'        

        elif 'cube' in display:
            try:
                number = display.replace('cube', '').strip()
                display = str(cube(int(number)))
            except (ValueError) as e:
                display = f'Error: {e}'

        elif 'sine' in display:
            try:
                number = display.replace('sine', '').strip()
                display = str(sine(float(number)))
            except (ValueError) as e:
                display = f'Error: {e}'  

        elif 'cos' in display:
            try:
                number = display.replace('cos', '').strip()
                display = str(cosine(float(number)))
            except (ValueError) as e:
                display = f'Error: {e}' 

        elif 'tangent' in display:
            try:
                number = display.replace('tangent', '').strip()
                display = str(tangent(float(number)))
            except (ValueError) as e:
                display = f'Error: {e}' 

        elif 'cot' in display:
            try:
                number = display.replace('cot', '').strip()
                display = str(cotangent(float(number)))
            except (ValueError) as e:
                display = f'Error: {e}' 

        elif 'cosec' in display:
            try:
                number = display.replace('cosec', '').strip()
                display = str(cosecant(float(number)))
            except (ValueError) as e:
                display = f'Error: {e}' 

        elif 'secant' in display:
            try:
                number = display.replace('secant', '').strip()
                display = str(secant(float(number)))
            except (ValueError) as e:
                display = f'Error: {e}'  

        elif 'log' in display:
            try:
                number = display.replace('log','').strip()
                display = str(log(float(number)))
            except (ValueError) as e:
                display = f'Error:{e}'     

        elif 'exp' in display:
            try:
                number = display.replace('exp','').strip()
                display = str(exponential(float(number)))
            except ValueError as e:
                display = f'Error:{e}'

        elif 'abs' in display:
            try:
                number = display.replace('abs','').strip()
                display = str(abs_fun(number))
            except ValueError as e:
                display = f'Error:{e}'

        return render(request, 'index.html', {'display': display})

    return render(request, 'index.html', {'display': ''})


