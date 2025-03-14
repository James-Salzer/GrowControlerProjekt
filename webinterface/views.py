from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html', {'message': 'Hallo, GrowController!'})

def button_click(request):
    if request.method == 'POST':
        return JsonResponse({'status': 'Button-Klick empfangen'})
    return JsonResponse({'status': 'Button-Klick empfangen'})

