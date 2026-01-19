import os
from datetime import datetime
from core.tts import speak

def system_status():
    username = os.environ.get("USERNAME")
    if os.name=="nt":
        os_name = "Windows"
    else:
        os_name = "Linux / macos"
    cwd = os.getcwd()
    
    info = f"""
    System Status:
    User: {username}
    Operating System : {os_name}
    Current Directory : {cwd}
    """
    print(info)
    speak(info)

def datetime_info():
    now = datetime.now()
    date = now.strftime("%d %B %Y")
    time = now.strftime("%I:%M %p")
    day = now.strftime("%A")
    reply=f"Today is {day}, {date}. Time is {time}"
    print(reply)
    speak(reply)