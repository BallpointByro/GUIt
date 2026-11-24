import subprocess as sp

# Standard push to repo
def push(commitMessage: str):
    sp.run(["git", "add", "."])
    sp.run(["git", "commit", "-m", f"{commitMessage}"])
    sp.run(["git", "push", "origin", "main"])

# Pulls from main branch
def pull():
    sp.run(["git", "pull"])

# DEVELOPER: Just so I don't have to type everything out so many times
if __name__ == "__main__":
    a = input("Enter your commit message: ")
    push(a)
