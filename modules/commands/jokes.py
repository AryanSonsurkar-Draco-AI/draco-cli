import random
from core.tts import speak

jokes_list =[
        "Why do programmers prefer dark mode? Because light attracts bugs.",
        "I told my computer I needed a break — now it won’t stop sending me KitKat ads.",
        "Real programmers count from 0.",
        "Why was the JavaScript developer sad? Because he didn’t know how to ‘null’ his feelings.",
        "A SQL query walks into a bar, walks up to two tables, and asks, “Can I join you?”",
        "My code works… I have no idea why.",
        "Debugging: being the detective in a crime you committed.",
        "I dream in Python, but I debug in nightmares."
    ]

def jokes(cmd):
    if "joke" in cmd:
        reply = random.choice(jokes_list)
        print(reply)
        speak(reply)