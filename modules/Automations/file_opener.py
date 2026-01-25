import os
import subprocess

SEARCH_PATHS = [
    os.path.join(os.environ["USERPROFILE"],"Desktop"),
    os.path.join(os.environ["USERPROFILE"],"Documents"),
    os.path.join(os.environ["USERPROFILE"],"Downloads"),
    os.path.join(os.environ["USERPROFILE"],"OneDrive")
]

def open_file_or_folder(cmd):
    cmd = cmd.replace("open","").replace("file","").replace("folder","").strip()
    for base_path in SEARCH_PATHS:
        for root, dirs, files in os.walk(base_path):
            for d in dirs:
                if cmd in d.lower():
                    folder_path = os.path.join(root,d)
                    os.startfile(folder_path)
                    return f"Opening folder: {d}"
            for f in files:
                if cmd in f.lower():
                    file_path = os.path.join(root,f)
                    os.startfile(file_path)
                    return f"Opening file: {f}"
    return "File or Folder not found."