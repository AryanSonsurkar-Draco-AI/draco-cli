import os
from core.tts import speak

NOTES_FILE = "notes.txt"

def notes(cmd):
    if "note add" in cmd:
        note = cmd.replace("note add","").strip()
        if note=="":
            reply="Please tell me what note to add."
            print(reply)
            speak(reply)

        with open(NOTES_FILE,"a") as f:
            f.write(note + "\n")

        reply ="Note added successfully."
        print(reply)
        speak(reply)

    elif "note show" in cmd:
        if not os.path.exists(NOTES_FILE):
            reply="No notes found."
            print(reply)
            speak(reply)
            return
        
        with open(NOTES_FILE,"r") as f:
            content=f.read().strip()

            if content=="":
                reply="Your notes are empty."
            
            else:
                reply="Here are your notes:\n" + content

                print(reply)
                speak("Showing your notes")

    elif "note clear" in cmd:
        open(NOTES_FILE,"w").close()
        reply="All notes cleared."
        print(reply)
        speak(reply)