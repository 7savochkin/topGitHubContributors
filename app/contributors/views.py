from django.http import HttpResponse


def main(request):
    return HttpResponse('<h1>Hello world!</h1>')
