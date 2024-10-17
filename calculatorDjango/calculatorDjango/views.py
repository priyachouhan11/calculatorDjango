# views.py

from django.shortcuts import render
from .Calculator import (
    cube_root, factorial, calculate_percentage, find_hcf, log, power_of_x, square, cube,
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

        elif 'cosine' in display:
            try:
                number = display.replace('cosine', '').strip()
                display = str(cosine(float(number)))
            except (ValueError) as e:
                display = f'Error: {e}' 

        elif 'tangent' in display:
            try:
                number = display.replace('tangent', '').strip()
                display = str(tangent(float(number)))
            except (ValueError) as e:
                display = f'Error: {e}' 

        elif 'cotangent' in display:
            try:
                number = display.replace('cotangent', '').strip()
                display = str(cotangent(float(number)))
            except (ValueError) as e:
                display = f'Error: {e}' 

        elif 'cosecant' in display:
            try:
                number = display.replace('cosecant', '').strip()
                display = str(cosecant(float(number)))
            except (ValueError) as e:
                display = f'Error: {e}' 

        elif 'secant' in display:
            try:
                number = display.replace('secant', '').strip()
                display = str(secant(float(number)))
            except (ValueError) as e:
                display = f'Error: {e}'         

        elif 'calculate_percentage' in display:
            try:
                numbers = display.replace('calculate_percentage', '').strip().split('%')
                if len(numbers) == 2:
                    score = float(numbers[0])
                    total = float(numbers[1])
                    display = str(calculate_percentage(int(score, total)))
                else:
                    display = "Error: Invalid input for percentage"
            except (ValueError, IndexError) as e:
                display = f'Error: {e}'

        elif 'log' in display:
            try:
                number = display.replace('log','').strip().split('log')
                if len(number) == 2:
                  base = int(number[0])
                  value = int(number[1])
                  display = str(log(float(base,value)))     
                else:
                    display = 'Error'
            except (ValueError,IndexError) as e:
                display = f'Error: {e}'            

        return render(request, 'index.html', {'display': display})

    return render(request, 'index.html', {'display': ''})


