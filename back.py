"""
#########################################
# GUIt - A visual representation of Git #
#########################################

Have YOU ever been interested in programming using powerful sources such as
GitHub? Are you limited by your sheer tech illiteracy? FEAR NO LONGER! Using
GUIt, you can code to your hearts content, and push it all to GitHub without
touching the command line!

Or if you are lazy, like me, this is a much better way to use git.

TO NOTE:
    - Because this version (.py extension) is a Proof Of Concept, not all features will be in this version
        - Watch for the rust version when I finish this POC.
    - Needs `gh auth` to be set up

##########
# BACK.PY
########
# Where the git commands are ran through subprocess
"""

##########
# Modules
########
import subprocess as sp

# Standard push to repo
def push(commitMessage: str):
    sp.run(["git", "add", "."], check=True)
    sp.run(["git", "commit", "-m", f"{commitMessage}"], check=True)
    sp.run(["git", "push", "origin", "main"], check=True)


# Pulls from main branch
def pull():
    sp.run(["git", "pull"], check=True)

# DEVELOPER: Just so I don't have to type everything out so many times
if __name__ == "__main__":
    a = input("Enter your commit message: ")
    push(a)
