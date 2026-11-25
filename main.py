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
# MAIN.PY
########
# Where the user initialises the repository to be passed into front.py
"""

##########
# Modules
########
import tkinter as tk
from tkinter import filedialog as fd

# Join Ruff Accordance (tf is that)
import back as gitbk # Backend (see back.py)
import front as gitfr # Frontend

##################
# Open the window
wn = tk.Tk()
wn.title("GUIt. Git, better")
winX = 800 ## Set window Sizes ##
winY = 450 ## Set window Sizes ##
wn.geometry(f"{winX}x{winY}")

# Repository path
repo = "" # See chooseGitDirectory() - gitbk Functions & Subroutines

#############
# GUIt Start
###########
# Hooks main.py into front.py
# main.py just acts as a menu screen
# front.py is the screen that is integrated the most into back.py

def guitStart():
    print("GUIt -> transfer from main.py into front.py")

################################
# gitbk Functions & Subroutines
##############################
# Functions and subroutines that connect to the backend (back.py)



##################
# Starting Screen
################
# In this menu, you can choose a repository (from a file manager), or clone one to a location

# Choose & Clone Repo Label
chooseGitDirectoryLabel = tk.Label(wn, text="Choose your git repository location:").place(x=200, y=275)
cloneRepoLabel = tk.Label(wn, text="Clone a Repository:").place(x=200, y=305)

# Choose & Clone Repo Entry
# Too tired to figure out how to use filedialog. Entry is better for POC (Written in Python before Rust)
choosegitDirectory = tk.Entry(wn).place()

continueButton = tk.Button(wn, text="Continue ->", command=guitStart).place(x=690, y=410)

#######################
# Keep the window open
wn.mainloop()
