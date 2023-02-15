import streamlit as st
import speech_recognition as sr
import os

def listen_microphone():
    microphone = sr.Recognizer()

    with sr.Microphone() as source:
        microphone.adjust_for_ambient_noise(source)
        st.info("Speak now...")
        audio = microphone.listen(source)

    try:
        phrase = microphone.recognize_google(audio, language='en-US')
        st.success("You said: {}".format(phrase))
    except sr.UnknownValueError:
        st.error("I didn't understand what you said.")
    except sr.RequestError as e:
        st.error("Could not request results from Google Speech Recognition service: {}".format(e))

st.title("Speech-to-Text")
st.write("Click the button and speak into your microphone to transcribe your speech to text.")

if st.button("Start Recording"):
    listen_microphone()
