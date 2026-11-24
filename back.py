import subprocess as sp

def push(commitMessage: str):
    sp.run(["git", "add", "."], check=True)
    sp.run(["git", "commit", "-m", f"{commitMessage}"])

push("back.py fix")
