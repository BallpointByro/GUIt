import subprocess as sp
import time as ti

def push(commitMessage):
    sp.run("git add .")
    ti.sleep(1)
    sp.run(f"git commit -m '{commitMessage}'")
    ti.sleep(1)
    sp.run("git push")
push("Test running back.py")
