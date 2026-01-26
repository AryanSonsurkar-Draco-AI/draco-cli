import subprocess

def ask_ollama(prompt):
    result = subprocess.run(
        ["ollama","run","llama3"],
        input=prompt,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="ignore"  
    )

    return result.stdout.strip()