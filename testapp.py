import streamlit as st
import sounddevice as sd
import speech_recognition as sr
import soundfile as sf
import time 
import tempfile
from src.sound import sound
import re
import os
from setting import DURATION,WAVE_OUTPUT_FILE,TEXT_OUTPUT_FILE
import numpy as np
from Api import CreateQuiz
r = sr.Recognizer()

def transcribe_voice(AUDIO_FILE,TEXT_FILE):
    with sr.AudioFile(AUDIO_FILE) as source:
         audio = r.record(source)
    text = r.recognize_google(audio)
    with open(TEXT_FILE, 'w') as file:
        file.write(text)
    return text 

if __name__ == "__main__":
    st.title("Microphone Recorder")
    if st.button('Record'):
        with st.spinner(f'Recording for {DURATION} seconds ....'):
            sound.record()
        st.success("Recording completed")
    if st.button('Play'):
        try:
            audio_file = open(WAVE_OUTPUT_FILE, 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/wav')
        except:
            st.write("Please record sound first")
    if st.button('Transcribe'):
        with st.spinner("Speech To Text"):
            text = transcribe_voice(WAVE_OUTPUT_FILE,TEXT_OUTPUT_FILE)
        st.success("Transcription completed")
        st.write("The tanscribed text is : ( "+text+" )")
        if text  == None:
            st.write("Please record sound first")
        st.write("\n")
    if st.button('Generate Quiz Link'):
        with st.spinner("Generating Quiz Link"):
            link = CreateQuiz(TEXT_OUTPUT_FILE)
        st.success("Google Quiz Form is Ready")
        st.write(link)

