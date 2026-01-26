from modules.Brain.web_apps import web_search, format_results
from modules.Ollama.ollama_helper import ask_ollama
from core.tts import speak

def draco_search(cmd):
    print("\nSearching the internet...")
    speak("Searching the internet")

    results = web_search(cmd)

    if not results:
        print("No results found.")
        speak("No results found.")
        return
    
    print("Analyzing results....")
    speak("Analyzing results")

    raw_data = format_results(results)

    prompt = f"""
You are Draco, an intelligent assistant.
Explain the following search results clearly and simply:
{raw_data}
Give a short, useful explanation.
"""
    summary = ask_ollama(prompt)

    print("\nDraco Says:\n")
    speak("Draco Says")
    print(summary)
    summary = summary[:600]
    speak(summary)