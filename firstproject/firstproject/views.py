from django.http import HttpResponse


def add(request):
    return HttpResponse("<h1>Welcome to addition </h1>")


def sub(request):
    return HttpResponse("<h1>Welcome to subtraction </h1>")


def mul(request):
    return HttpResponse("<h1>Welcome to Multiplication </h1>")


def div(request):
    return HttpResponse("<h1>Welcome to Division </h1>")