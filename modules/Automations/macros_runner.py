import json
import os
import time

MACRO_FILE = os.path.join("macros.json")

def load_macros():
    if not os.path.exists(MACRO_FILE):
        return {}
    with open(MACRO_FILE, "r") as f:
        return json.load(f)

def list_macros():
    macros = load_macros()
    if not macros:
        print("No macros found.")
        return
    print("Available macros:")
    for name in macros:
        print(f"- {name}")

def show_macro(name):
    macros = load_macros()
    if name not in macros:
        print("Macro not found.")
        return
    print(f"Macro '{name}':")
    for cmd in macros[name]:
        print(f"  → {cmd}")

def run_macro(name, command_executor):
    macros = load_macros()
    if name not in macros:
        print("Macro not found.")
        return

    print(f"Running macro: {name}\n")

    for cmd in macros[name]:
        print(f"→ Running: {cmd}")
        try:
            command_executor(cmd)
            print("✔ Done\n")
        except Exception as e:
            print(f"✖ Failed: {e}\n")
        time.sleep(0.5)
