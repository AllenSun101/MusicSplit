from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from split import separate
from transcribe import getMIDI
from yt_to_mp3 import convert_yt_to_mp3
from django.middleware.csrf import get_token
import json

# Create your views here.

def say_hello(request):
    print("YAY")
    return JsonResponse({"message": 'Hello World'})

def yt_to_mp3(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        link = data.get('link', None)
        if link:
            file_path = convert_yt_to_mp3(link)
            # Convert the file path to a public URL
            file_url = request.build_absolute_uri(f'/media/{file_path}')
            return JsonResponse({"output": file_url}, safe=False)
        return JsonResponse({"error": "No link provided"}, status=400)


def split_mp3(request):    
    audio_path = request.GET.get('audio_path', None)
    stems = request.GET.get('stems', None)

    return JsonResponse({"output": separate(audio_path, stems)}, safe=False)

def mp3_to_midi(request):
    if request.method == 'POST':
        file = request.FILES['files[]']
        if file:
            file_path = getMIDI(file)
            # Convert the file path to a public URL
            file_url = request.build_absolute_uri(file_path)
            return JsonResponse({"output": file_url}, safe=False)
        return JsonResponse({"error": "No file provided"}, status=400)
    
def join_stems(request):
    audio_paths = request.GET.get('audio_path', None)

    return JsonResponse({"output": split_mp3(audio_paths)}, safe=False)

def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrfToken': csrf_token})