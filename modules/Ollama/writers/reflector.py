import subprocess
from core.tts import speak

def reflect():
    print("\nDraco - Daily Reflection\n")
    speak("Draco - Daily Reflection")

    speak("What did you work on today?")
    ans1 = input("\n1. What did you work on today?\n")

    speak("What went well today?")
    ans2 = input("\n2. What went well today?\n")

    speak("What didn't go well?")
    ans3 = input("\n3. What didn't go well?\n")

    print("\nAnalyzing your day....\n")
    speak("Analyzing your day....")

    prompt = (
        f"""You are a productivity assistant named Draco.
            Based on the user's daily reflection, do the following:
            1. Write a short, honest summary of the day (2-3 bullet points)
            2. Identify one strength shown today
            3. Identify one weakness or improvement area
            4. Suggest 2 clear focus points for tomorrow
            Be practical,direct, and motivating.
            No emojis. No fluff.

            Daily Reflection:
            Work done: {ans1}
            What went well: {ans2}
            What went wrong: {ans3}
        """
    )
    result = subprocess.run(
        ["ollama","run","llama3"],
        input=prompt,
        text=True,
        encoding="utf-8",
        errors="ignore",
        capture_output=True
    )
    return result.stdout.strip()