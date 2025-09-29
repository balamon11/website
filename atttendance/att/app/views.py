from django.shortcuts import render
from django.http import HttpResponse
def view1(request):
    html = "<h1>Hala Madrid Ina Da Mas</h1><p>Real Madrid Will Win The UCL</p>"
    return HttpResponse(html)

def view2(request):
    return render(request,'home.html')