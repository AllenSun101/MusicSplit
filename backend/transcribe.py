from basic_pitch.inference import predict_and_save, Model
from basic_pitch import ICASSP_2022_MODEL_PATH
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

def getMIDI(file):

    input_dir = os.path.join(os.getcwd(), 'temp_files')

    fs = FileSystemStorage(location=input_dir)
    filename = fs.save(file.name, file)
    file_path = fs.path(filename) 


    output_dir = os.path.join(os.getcwd(), 'media/midi')  

    basic_pitch_model = Model(ICASSP_2022_MODEL_PATH)

    predict_and_save([file_path], model_or_model_path=basic_pitch_model, output_directory=output_dir, 
                     save_midi=True, sonify_midi=False, save_model_outputs=False, save_notes=False)
    
    base, ext = os.path.splitext(filename) 
    output_file_name = base + '_basic_pitch.mid'

    # Create a public URL for the output MIDI file
    output_file_url = os.path.join(settings.MEDIA_URL, 'midi', output_file_name)

    return output_file_url


# getMIDI("output\Welcome_To_New_Yorke\\other.wav")

