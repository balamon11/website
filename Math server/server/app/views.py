from django.shortcuts import render

# Create your views here.
def maths(request):
    result ='________'
    if request.method == "POST":
        try:
            I = float(request.POST.get("intensity"))
            R = float(request.POST.get("resistance"))
            result = (I ** 2) * R
        except:
            result = "Invalid input"
    return render(request,'math.html',{"result": result})