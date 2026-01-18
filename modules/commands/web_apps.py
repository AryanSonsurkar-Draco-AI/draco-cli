import webbrowser
from core.tts import speak

def web_commands(cmd):
    if cmd=="open chatgpt":
        reply = "Opening ChatGPT"
        print(reply)
        speak(reply)
        webbrowser.open("https://chatgpt.com")
    
    elif cmd=="open github":
        reply = "Opening GitHub ,Bro commit well!"
        print(reply)
        speak(reply)
        webbrowser.open("https://github.com")
        
    elif cmd=="open youtube":
        reply = "Opening Youtube"
        print(reply)
        speak(reply)
        webbrowser.open("https://youtube.com")
    
    elif cmd=="open instagram":
        reply = "Opening Instagram"
        print(reply)
        speak(reply)
        webbrowser.open("https://instagram.com")

    elif cmd=="open leetcode":
        reply = "Opening Leetcode,Bro glad you are finally gonna do DSA."
        print(reply)
        speak(reply)
        webbrowser.open("https://leetcode.com")

    elif cmd=="open google":
        reply = "Opening Google"
        print(reply)
        speak(reply)
        webbrowser.open("https://google.com")    
    
    elif cmd=="open bing":
        reply = "Opening bing"
        print(reply)
        speak(reply)
        webbrowser.open("https://bing.com")

    elif cmd=="open discord":
        reply = "Opening Discord, let's find fellow programmers."
        print(reply)
        speak(reply)
        webbrowser.open("https://discord.com")

    else:
        reply ="Sorry i can't open it"
        print(reply)
        speak(reply)