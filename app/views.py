from django.shortcuts import render

# Create your views here.
def rendering(request):
    return render(request,'rendering.html')
