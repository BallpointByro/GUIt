"""#########################################
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

###########
# FRONT.PY
#########
# The script where the user actually interacts with Git.
"""

##########
# Modules
########
import tkinter as tk


#################
# Repo Directory
###############
repo = ""

#############
# GUIt Class
###########
# Where everything happens
class guitFront:
    def __init__(self):
        # Initialise window
        self.wn = tk.Tk()
        self.wn.title("GUIt Frontend")
        self.wn.geometry("800x450")
        self.wn.mainloop()


if __name__ == "__main__":
    print("Running from terminal (called by author)")
    guitFront()
else:
    print(f"Running from {__name__}")
