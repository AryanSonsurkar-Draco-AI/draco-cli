import webbrowser
from core.tts import speak
from ddgs import DDGS

def web_search(cmd,max_result=5):
    results=[]

    with DDGS() as ddgs:
        for r in ddgs.text(cmd,max_result=max_result):
            results.append({
                "title": r.get("title",""),
                "body": r.get("body",""),
                "link": r.get("href","")
            })
    
    return results

def format_results(results):
    text = ""
    for i,r in enumerate(results,start=1):
        text+=f"""
        Result {i}:
        Title: {r['title']}
        Info: {r['body'] if r['body'] else "No description available"}
        """
    return text.strip()

def web_commands(cmd):
    if cmd=="open website chatgpt":
        reply = "Opening ChatGPT"
        print(reply)
        speak(reply)
        webbrowser.open("https://chatgpt.com")
    
    elif cmd=="open website github":
        reply = "Opening GitHub ,Bro commit well!"
        print(reply)
        speak(reply)
        webbrowser.open("https://github.com")
        
    elif cmd=="open website youtube":
        reply = "Opening Youtube"
        print(reply)
        speak(reply)
        webbrowser.open("https://youtube.com")
    
    elif cmd=="open website instagram":
        reply = "Opening Instagram"
        print(reply)
        speak(reply)
        webbrowser.open("https://instagram.com")

    elif cmd=="open website leetcode":
        reply = "Opening Leetcode,Bro glad you are finally gonna do DSA."
        print(reply)
        speak(reply)
        webbrowser.open("https://leetcode.com")

    elif cmd=="open website google":
        reply = "Opening Google"
        print(reply)
        speak(reply)
        webbrowser.open("https://google.com")    
    
    elif cmd=="open website bing":
        reply = "Opening bing"
        print(reply)
        speak(reply)
        webbrowser.open("https://bing.com")

    elif cmd=="open website discord":
        reply = "Opening Discord, let's find fellow programmers."
        print(reply)
        speak(reply)
        webbrowser.open("https://discord.com")

    else:
        reply ="Sorry i can't open it"
        print(reply)
        speak(reply)