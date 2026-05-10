import wave
import numpy as np

def analyze_audio(audio_file):
    # Simplified: detect if RMS > threshold (talking)
    wf = wave.open(audio_file, 'rb')
    frames = wf.readframes(wf.getnframes())
    audio = np.frombuffer(frames, dtype=np.int16)
    rms = np.sqrt(np.mean(audio**2))
    return rms > 2000  # threshold