from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def say_hello(request):
    return HttpResponse('Hello World')


def get_campaigns(request):    
    authors = request.GET.get('authors', None)

    data = {}

    # Return the data as JSON response
    return JsonResponse(data, safe=False)
