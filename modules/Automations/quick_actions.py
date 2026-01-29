import os
import webbrowser
import subprocess 
from core.tts import speak

def open_study_setup():
    webbrowser.open("https://www.google.com")
    webbrowser.open("https://www.youtube.com")
    print("Study setup ready.")
    speak("Study setup ready.")

def open_coding_setuo():
    subprocess.Popen("code",shell=True)
    webbrowser.open("https://github.com")
    print("Coding setup ready.")
    speak("Coding setup ready.")

def open_exam_setup():
    subprocess.Popen("calc")
    print("Exam prep mode activated.")
    speak("Exam prep mode activated.")