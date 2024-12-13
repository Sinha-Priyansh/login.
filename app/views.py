from django.shortcuts import render

# Create your views here.
def kohli(request):
    return render(request,'project11.html')

def details(request):
    return render(request,'kohli_det.html')