import os
from pathlib import Path
os.system("pip install streamlit")
from kora import ngrok


def start(script=None):
    """ run the script and connect with ngrok"""
    if script is None:
        script = guess_file()
    url = ngrok.connect(8501).public_url
    print(url)
    os.system(f"streamlit run {script} --server.runOnSave=true &")


def stop():
    ngrok.kill()
    os.system("pkill streamlit")


def guess_file():
    for fn in ["main.py", "app.py", "hello.py"]:
        if Path(fn).exists():
            return fn
    # the first .py in current directory
    return next(Path().glob("*.py"))
