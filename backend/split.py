from spleeter.separator import Separator
import os
from dotenv import load_dotenv


def separate(song, stems) -> bool:
    if song is None or stems is None:
        return False
    
    load_dotenv()
    ffmpeg_path = os.environ.get("FFMPEG_PATH")

    # Set the PATH environment variable to include FFmpeg's bin directory
    os.environ['PATH'] += os.pathsep + ffmpeg_path

    audio_path = f'{song}'

    # Initialize Spleeter separator
    separator = Separator(f'spleeter:{stems}stems')

    # Separate the audio file
    output_dir = os.path.join(os.getcwd(), 'output')  
    separator.separate_to_file(audio_path, output_dir)

    return True


def join(file_paths):
    pass


if __name__ == '__main__':
    # Define the input file
    # input_file = 'I_Think_He_Knows.mp3'

    # Perform the separation
    # separate(input_file, 2)
    pass