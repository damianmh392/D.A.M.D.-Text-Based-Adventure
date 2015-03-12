#D.A.M.D. Text Based Adventure
#BY:
#   Damian Manning-Henseler
#   Andrew Roundtree
#   Micah Belden
#   Deryk Patraw




########## GIT CODE NEEDED ##########
'''

cd 'program directory'
git pull origin master
    #####work on program#####
git add .
git status
git commit -m "state what you did for the program"
git status
git push origin master

'''






from tkinter import *
import tkinter.simpledialog
import tkinter.messagebox

root = Tk()
w = Label(root, text="A D.A.M.D. Adventure")
w.pack()

###Intro###
def intro():
    messagebox.showinfo("The Crossroads","You wake up in a four way intersection. there are small dirt" +
                        " paths in a field, one going North, one South, one East, and one West. Which" +
                        " path do you wish to choose?")
    path = simpledialog.askstring("Where to Go","Type ""North"" to go north and so on to choose your path.")
    if path == "North":
        north()

    elif path == "South":
        south()

    elif path == "East":
        east()

    elif path == "West":
        west()

    else:
        intro()    


###Damian's Functions###
def south():
    messagebox.showinfo("South","You headed down the south path and arive at a large city after a lengthy" +
                        " trek. You walk into the bustling city and shortly after a hobo aproches you." +
                        " This decrepid man in tattered clothes askes you ''You! Do you want some beans?" +
                        " They're great, I guarantee they're quality beans!''")
    simpledialog.askstring("","")
    


###Andrew's Functions###
#lets start how to do this thing#
def east():
    messagebox.showinfo("East"," Your journey begins as of now yet there is still yet a chance"+
                        "to turn back if you so choose "+
                        "but only a coward turns back from any adventure presented to him." )
    goback = simpledialog.askstring("turn back?"," Do you desire a different path?")
    if goback == "yes":
        intro()
    else:
        east()                
                           


###Micah's Functions###
def west():
    messagebox.showinfo("","")

###Deryk's Functions###
def north():
    messagebox.showinfo("","")


### Main ###
intro()

root.destroy()        
        


