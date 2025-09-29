from django.shortcuts import render

# Create your views here.
def fun(a):
    return render(a,"map.html")
def rail(a):
    return render(a,"rail.html")
def rpc(a):
    return render(a,"rpc.html")
def metro(a):
    return render(a,"metro.html")
def th(a):
    return render(a,"theatre.html")
def beach(a):
    return render(a,"beach.html")