import subprocess as sp

def push(commitMessage: str):
    sp.run(["git", "add", "."], check=True)
    sp.run(["git", "commit", "-m", f"{commitMessage}"])
    sp.run(["git", "push", "origin", "main"])

if __name__ == "__main__":
    a = input("Enter your commit message: ")
    push(a)
