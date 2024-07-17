from spleeter.separator import Separator
import os

def separate(song):
    """if audio_file is None:
        return jsonify({'error': 'No audio file provided'}), 400

    audio_path = f'/tmp/{song}'
    audio_file.save(audio_path)"""

    # Set the PATH environment variable to include FFmpeg's bin directory
    ffmpeg_path = r'C:\Users\allen\Downloads\ffmpeg-7.0.1-essentials_build\ffmpeg-7.0.1-essentials_build\bin'  # Adjust this path to the location of FFmpeg
    os.environ['PATH'] += os.pathsep + ffmpeg_path

    # Verify that FFmpeg is in the PATH
    assert any(os.path.isfile(os.path.join(p, 'ffmpeg.exe')) for p in os.environ['PATH'].split(os.pathsep)), "FFmpeg binary not found in PATH"


    audio_path = f'{song}'

    # Initialize Spleeter separator
    separator = Separator('spleeter:4stems')

    # Separate the audio file
    output_dir = os.path.join(os.getcwd(), 'output')  
    separator.separate_to_file(audio_path, output_dir)

    # return jsonify({'message': 'Separation done!'})



if __name__ == '__main__':
    # Define the input file
    input_file = 'Welcome_To_New_Yorke.mp3'

    # Ensure the output directory exists
    if not os.path.exists('output'):
        os.makedirs('output')

    # Perform the separation
    separate(input_file)