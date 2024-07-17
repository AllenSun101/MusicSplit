import os 
import librosa
import music21 as m21

# Step 2: Extract features using librosa
def extract_audio_features(wav_path):
    y, sr = librosa.load(wav_path)
    onset_env = librosa.onset.onset_strength(y=y, sr=sr)
    onset_times = librosa.onset.onset_detect(onset_envelope=onset_env, sr=sr, units='time')
    pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
    return onset_times, pitches, magnitudes, sr

# Step 3: Transcription using madmom (or custom logic)
def transcribe_audio(onset_times, pitches, magnitudes, sr):
    # Simplified example, more complex logic needed for accurate transcription
    notes = []
    max_frame = magnitudes.shape[1]
    for onset in onset_times:
        # Find the strongest pitch at the onset time
        onset_frame = int(onset * sr)
        if onset_frame >= max_frame:
            continue  # Skip onsets that are out of bounds
        pitch_idx = magnitudes[:, int(onset * sr)].argmax()
        pitch = pitches[pitch_idx, int(onset * sr)]
        if pitch > 0:
            note = m21.note.Note()
            note.pitch.frequency = pitch
            note.quarterLength = 1.0  # Simplified, set a fixed length
            notes.append(note)
    return notes

# Step 4: Generate sheet music using music21
def generate_sheet_music(notes, output_path):
    stream = m21.stream.Stream(notes)
    stream.write('musicxml', fp=output_path)

# Main function
def main(wav_path, output_path):
    onset_times, pitches, magnitudes, sr = extract_audio_features(wav_path)
    notes = transcribe_audio(onset_times, pitches, magnitudes, sr)
    generate_sheet_music(notes, output_path)

# Paths
output_dir = os.path.join(os.getcwd(), 'output')  
wav_path = os.path.join(output_dir, 'Blank_Space/accompaniment.wav')
output_path = os.path.join(output_dir, 'Blank_Space.xml')

# Run the process
main(wav_path, output_path)
