from matplotlib.pyplot import cla
from transformers import AutoProcessor, AutoModelForCTC
import torch

import os
import torchaudio

import speech_recognition as sr


# processor = AutoProcessor.from_pretrained("airesearch/wav2vec2-large-xlsr-53-th")

# model = AutoModelForCTC.from_pretrained("airesearch/wav2vec2-large-xlsr-53-th")

# class SR_Model:
#     def __init__(self,audio):
#         self.audio = audio

#     def get_audio(self):
#         speech, sr = torchaudio.load(self.audio)
#         speech = speech.squeeze()
#         resampler = torchaudio.transforms.Resample(sr, 16000)
#         speech = resampler(speech)
#         #print(speech.shape)
#         input_values = processor(speech, return_tensors="pt", sampling_rate=16000)["input_values"] #[0]
#         #print(input_values)
#         #input = input_values.reshape((input_values.shape[0],input_values.shape[2],input_values.shape[1]))
#         logits = model(input_values) #["logits"]
#         #print(logits)
#         predicted_ids = torch.argmax(logits["logits"], dim=-1)
#         #print(predicted_ids)
#         transcription = processor.decode(predicted_ids[0])
#         print(transcription)
#         return transcription

class Google_SR:
    def __init__(self,audio):
        self.audio = audio

    def use_asr(self):
        recog = sr.Recognizer()
        audio_file_ = sr.AudioFile(self.audio)
        with audio_file_ as source:
            audio_file = recog.record(source, duration = 7.0)
            result = recog.recognize_google(audio_data=audio_file, language='th')
        return result
        
