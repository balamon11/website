from django.shortcuts import render

# Create your views here.
def map(request):
    return render(request,"map.html")
def rail(request):
    return render (request,"rail.html")
def rpc(request):
    return render(request,"rpc.html")
def metro(request):
    return render(request,"metro.html")
def theatre(request):
    return render(request,"theatre.html")
def beach(request):
    return render(request,"beach.html")