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

"""

##########
# Modules
import tkinter as tk
from tkinter import filedialog as fd

# Join Ruff Accordance (tf is that)
import back as gitbk # Backend (see back.py)

##################
# Open the window
wn = tk.Tk()
wn.title("GUIt. Git, better")
winX = 800 ## Set window Sizes ##
winY = 450 ## Set window Sizes ##
wn.geometry(f"{winX}x{winY}")

# Repository path
repo = "" # See chooseGitDirectory() - gitbk Functions & Subroutines

################################
# gitbk Functions & Subroutines
##############################
# Functions and subroutines that connect to the backend (back.py)

def chooseGitDirectory():
    """
    chooseGitDirectory

    Opens the the Directory
    """
    global repo

    print("ADD CODE HERE INVOLVING REPO VAR")
    repo = "I tried"


#####################
# GUIT - Main script
###################
# What you all came for.
# A visual representation of Git for those who have no clue on how to use it.
class GUIt:
    def __init__(self, x):
        self.x = x

def guitStart():
    pass

##################
# Starting Screen
################
# In this menu, you can choose a repository (from a file manager), or clone one to a location

# Choose & Clone Repo Label

chooseGitDirectoryLabel = tk.Label(wn, text="Choose your git repository location:").place(x=200, y=275)
cloneRepoLabel = tk.Label(wn, text="Clone a Repository:").place(x=200, y=305)

chooseGitDirectoryButton = tk.Button(wn, text="Find Directory", command=chooseGitDirectory).place(x=450, y=270)

continueButton = tk.Button(wn, text="Continue ->", command=guitStart).place()

#######################
# Keep the window open
wn.mainloop()
