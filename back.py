import subprocess as sp

def push(commitMessage: str):
    sp.run(["git", "add", "."], check=True)
    sp.run(["git", "commit", "-m", f"{commitMessage}"])
    sp.run(["git", "push", "origin", "main"])

push("back.py fix 2")
