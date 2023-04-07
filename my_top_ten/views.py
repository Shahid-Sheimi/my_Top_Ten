from django.shortcuts import redirect,render

def Index(request):
    return render(request,'index.html')
