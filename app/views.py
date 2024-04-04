from django.shortcuts import render

# Create your views here.
def conditional(request):
    d={'a':100,'b':400,'c':300}
    return render(request,'conditional.html',d)