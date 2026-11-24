"""
#########################################
# GUIt - A visual representation of Git #
#########################################

Have YOU ever been interested in programming using powerful sources such as
GitHub? Are you limited by your sheer tech illiteracy? FEAR NO LONGER! Using
GUIt, you can code to your hearts content, and push it all to GitHub without
touching the command line!

Or if you are lazy, like me, this is a much better way to use git.

"""

##########
# Modules
import tkinter as tk
from PIL import ImageTk as pitk
from PIL import Image as pii
import back # Backend (see back.py)

##################
# Open the window
wn = tk.Tk()
wn.title("GUIt. Git, better")
winX = 800 ## Set window Sizes ##
winY = 450 ## Set window Sizes ##
wn.geometry(f"{winX}x{winY}")

# Repository path
repo = ""


##################
# Starting Screen
################
# In this menu, you can choose a repository (from a file manager), or clone one to a location

# Logo
logoPath = "assets/logo.svg" # Path
img = pitk.ImageTk.PhotoImage(pii.Image.open(logoPath)) # FIX HERE (yes, gitblame me!)
logoLabel = tk.Label(wn, image=img).place(x=400, y=200)


# Choose & Clone Repo Label
chooseRepoLabel = tk.Label(wn, text="Choose a Repository:").place(x=200, y=275)
cloneRepoLabel = tk.Label(wn, text="Clone a Repository:").place(x=200, y=305)

#######################
# Keep the window open
wn.mainloop()
