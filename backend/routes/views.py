from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from split import separate
from transcribe import getMIDI
from yt_to_mp3 import yt_to_mp3

# Create your views here.

def say_hello(request):
    return HttpResponse('Hello World')

def yt_to_mp3(request):
    # Return link to the saved file for download
    link = request.GET.get('link', None)

    return JsonResponse({"output": yt_to_mp3(link)}, safe=False)

def split_mp3(request):    
    audio_path = request.GET.get('audio_path', None)
    stems = request.GET.get('stems', None)

    return JsonResponse({"output": separate(audio_path, stems)}, safe=False)

def mp3_to_midi(request):
    audio_path = request.GET.get('audio_path', None)

    return JsonResponse({"output": split_mp3(audio_path)}, safe=False)

def join_stems(request):
    audio_paths = request.GET.get('audio_path', None)

    return JsonResponse({"output": split_mp3(audio_paths)}, safe=False)
