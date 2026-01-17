import webbrowser
from core.tts import speak

def web_commands(cmd):
    if cmd=="open chatgpt":
        reply = "Opening ChatGPT"
        print(reply)
        speak(reply)
        webbrowser.open("https://chatgpt.com")
    
    else:
        reply ="Sorry i can't open it"
        print(reply)
        speak(reply)