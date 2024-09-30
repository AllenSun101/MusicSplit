from spleeter.separator import Separator
import os
from dotenv import load_dotenv
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from pydub import AudioSegment

def separate(file, stems):
    if file is None or stems is None:
        return False
    
    input_dir = os.path.join(os.getcwd(), 'temp_files')

    fs = FileSystemStorage(location=input_dir)
    filename = fs.save(file.name, file)
    file_path = fs.path(filename) 
    
    load_dotenv()
    ffmpeg_path = os.environ.get("FFMPEG_PATH")

    # Set the PATH environment variable to include FFmpeg's bin directory
    os.environ['PATH'] += os.pathsep + ffmpeg_path

    audio_path = f'{file_path}'

    # Initialize Spleeter separator
    separator = Separator(f'spleeter:{stems}stems')

    # Separate the audio file
    output_dir = os.path.join(os.getcwd(), 'media/split')  
    separator.separate_to_file(audio_path, output_dir)

    # Get the base name and extension
    base, ext = os.path.splitext(filename)

    # Get a list of all files in the output directory
    separated_files = os.listdir(output_dir + "/" + base)

    output_file_urls = []

    for split_filename in separated_files:
        # Create the public URL for the output file
        output_file_url = os.path.join(settings.MEDIA_URL, 'split', base, split_filename)  # Include the filename

        # Append the output URL to the list
        output_file_urls.append(output_file_url)

    return output_file_urls


def join(files):
    audio1 = AudioSegment.from_file(files[0])
    audio2 = AudioSegment.from_file(files[1])

    mixed_audio = audio1.overlay(audio2)

    output_file = os.path.join(os.getcwd(), 'media/join', 'mixed_audio.mp3')  

    mixed_audio.export(output_file, format="mp3")

    output_file_url = os.path.join(settings.MEDIA_URL, 'join', 'mixed_audio.mp3')

    return output_file_url


if __name__ == '__main__':
    # Define the input file
    # input_file = 'I_Think_He_Knows.mp3'

    # Perform the separation
    # separate(input_file, 2)
    pass