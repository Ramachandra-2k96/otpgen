from django.shortcuts import render
from .forms import inputform
from django.http import JsonResponse
import random
# Create your views here.

def home(request):
    form = inputform()  # Instantiate form by default
    if request.method == "POST":
        form = inputform(request.POST)
    return render(request, 'app1/index.html', {"form": form})

def generateOTP(request):
    if request.method == "POST":
        form = inputform(request.POST)
        if form.is_valid():
            list1=[]
            quantity = form.cleaned_data.get('quantity')
            size = form.cleaned_data.get('size')
            for i in range(1,quantity+1):
                list1.append(random.randint(10**(size-1),10**size-1))
            return JsonResponse({'param1': list1})
        else:
            return JsonResponse({'error': 'Form data is invalid'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405) 