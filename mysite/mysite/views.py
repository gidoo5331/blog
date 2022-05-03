from django.shortcuts import render

# React frontEnd Build View
def react(request):
    return render(request, "index.html")

# def react(request):
#     context = { }
#     return render(request, "index.html", context)