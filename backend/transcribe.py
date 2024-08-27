from basic_pitch.inference import predict_and_save, Model
from basic_pitch import ICASSP_2022_MODEL_PATH
import os

def getMIDI(file):

    output_dir = os.path.join(os.getcwd(), 'midi')  

    basic_pitch_model = Model(ICASSP_2022_MODEL_PATH)

    predict_and_save([file], model_or_model_path=basic_pitch_model, output_directory=output_dir, 
                     save_midi=True, sonify_midi=False, save_model_outputs=False, save_notes=False)


# getMIDI("output\Welcome_To_New_Yorke\\other.wav")

