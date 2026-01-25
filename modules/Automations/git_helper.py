import subprocess

def git_push(cmd):
    cmd = cmd.replace("git push with message","")
    prompt = (
        f"You are draco CLI automation assistant.Convert the user intent into clean terminal commands.DO NOT EXPLAIN.Return only commands.USer intent is to git push with this msg,make sure to add all files then commit then push.The message is {cmd}"
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

def git_repo():
    prompt = (
        "You are draco CLI automation assistant.Convert the user intent into clean terminal commands.DO NOT EXPLAIN.Return only commands.USer intent is to create a new repo ,make sure to git init then add all files then initial commit then git branch main then git remote add origin <repo_url> then push to origin main."
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