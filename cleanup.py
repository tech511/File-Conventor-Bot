import shutil
import os

def cleanup():

    if os.path.exists("downloads"):
        shutil.rmtree("downloads")

    if os.path.exists("output"):
        shutil.rmtree("output")

    os.makedirs("downloads", exist_ok=True)
    os.makedirs("output", exist_ok=True)
