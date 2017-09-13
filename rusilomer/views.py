from django.shortcuts import render

def index(request):
    # return redirect('index')
    return render(request, 'index.html')