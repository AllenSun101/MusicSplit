from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from split import separate
from transcribe import getMIDI
from yt_to_mp3 import convert_yt_to_mp3
from django.middleware.csrf import get_token
import json
import os
import zipfile
from django.conf import settings

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
    if request.method == 'POST':
        file = request.FILES['files[]']
        stems = request.POST.get('stems')
        if file and stems:
            file_paths = separate(file, stems)

            zip_filename = 'stems.zip'
            zip_path = os.path.join(settings.MEDIA_ROOT, "split", zip_filename)  # Adjust the path as needed

            # Create a ZIP file
            with zipfile.ZipFile(zip_path, 'w') as zipf:
                for file_url in file_paths:
                    zipf.write(os.getcwd() + "/" + file_url, os.path.basename(file_url))
            
            zip_file_url = os.path.join(settings.MEDIA_URL, 'split', zip_filename)  # Construct the public URL

            return JsonResponse({"output": request.build_absolute_uri(zip_file_url)})
        return JsonResponse({"error": "No file or stem number provided"}, status=400)


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
