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
    path = simpledialog.askstring("Where to Go","Type the direction you wish to go, choose your path. your options are ''North, South, East, and West''")
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
    messagebox.showinfo("South","You headed down the south path and arive at a fork in the road. One" +
                        " fork leads to a large mountian, practicallly untouched by man, and the other" +
                        " to a busy city full of people.")
    approch = simpledialog.askstring("Where Now?","Do you want to go to the City or the Mountian?" +
                                     " (Mountian/City)")
    if approch == "City":
        city()
    elif approch == "Mountian":
        mountains()
    else:
        south()

def city():
    messagebox.showinfo("City","You walk into the bustling city and shortly after a hobo aproches you." +
                        " This decrepid man in tattered clothes askes you ''You! Do you want some beans?" +
                        " They're great, I guarantee they're quality beans!''")
    approch = simpledialog.askstring("Beans?","Do you accept the hobo's beans? (Yes/No)")
    if beans == "Yes":
        yesbeans()
    elif beans == "No":
        nobeans()
    else:
        city()        

def mountains():
    messagebox.showinfo("Mountian","You trek to the mountian and find yourself at home. you decide to live" +
                        " there as a mountian hermit. After several months of living on the mountain, you" +
                        " are approched by Sassquach. The massive creature approches you, it groans and" +
                        " whoops at you, and then waits for a reply"
    reply = simpledialog.askstring("Don't Sass the Quatch","How do you want to resond to Sassquatch's" +
                                   " 'question'. (Whoop/Groan)")
    if reply == "Whoop":
        jacklinks()
    elif reply == "Groan":
        sassed()                
                        
    

    

###Andrew's Functions###
#lets start how to do this thing#
def east():
    messagebox.showinfo("East"," Your journey begins as of now. Yet there is still yet a chance"+
                        " to turn back, if you so choose but only a coward turns back from any"+
                        " adventure presented to him." )
    goback = simpledialog.askstring("turn back?"," Do you desire a different path?")
    if goback == "yes":
        intro()
    elif goback == "no":
        easternjourney()
    else:
        east()                

def easternjourney():
    messagebox.showinfo("Mountainous Ruins","you see in the disatance a lone Mountain and you"+
                        " can make it there by nightfall, but you also see possible ruins, such"+
                        " a place could hold a mighty treasure. however with the mountain such a large"+
                        " area must hold an ancient secret... Which do you choose to go? there is"+
                        " still an oppertunity to turn back. but it is the last chance todo so.")
    
    mtruins = simpledialog.askstring("What is your decision?","you can 'go back', 'mountain', or 'ruins'")
    if mtruins == "go back":
        east()
    elif mtruins == "mountain":
        mountain()
    elif mtruins == "ruins":
        ruins()
    else:
        easternjourney()


   

###Micah's Functions###
def west():
    messagebox.showinfo("","")

###Deryk's Functions###

global goback
goback = 0

def north():
    if goback == 0:
        messagebox.showinfo("North","You decide to go north. After a few hours of walking, your path ends. Before you is a " +
                            "dock, with a large, wooden ship, masts and all, with crew bustling around it. There is also" +
                            " a long coastline you can walk along if you so choose.")
    else:
        messagebox.showinfo("North","You decide to go back onto the beach. Before you is a " +
                            "dock, with a large, wooden ship, masts and all, with crew bustling around it. There is also" +
                            " a long coastline you can walk along if you so choose.")

    shipchoice = simpledialog.askstring("Where do you go?","Would you like to 'board' the ship, 'walk' the coastline, or 'go back' to the intersection?")

    if shipchoice == "board":
        ship()
    elif shipchoice == "walk":
        coast()
    elif shipchoice == "go back":
        intro()
    else:
        north()

def ship():
    messagebox.showinfo("Board the ship","You have boarded the ship. All the crew stops what they're doing and look at you curiously.")
    boardchoice = simpledialog.askstring("What do you do?","You can 'request' a ride, attempt to 'take over' the ship, or you can avoid the awkwardness and 'go back'.")

    if boardchoice == "request":
        sail()
    elif boardchoice == "take over":
        pirate()
    elif boardchoice == "go back":
        global goback
        goback = 1
        north()
    else:
        ship()

def coast():
    coastchoice = simpledialog.askstring("Walk the coast","You decide to walk the coast. Do you wish to go 'left', 'right', or 'go back'?")

    if coastchoice == "left":
        left()
    elif coastchoice == "right":
        right()
    elif coastchoice == "go back":
        global goback
        goback = 1
        north()
    else:
        coast()

def left():
    messagebox.showinfo("Left","You decide to walk the coast. It's actually really peaceful, and you have a lot of time to think. You begin to think about yourself." +
                        " Who are you anyway? You woke up in a fork in the road, with no memory of how you got there, who you are, and especially, why you're here.")
    messagebox.showinfo("Left", "Why are you here? Is it happenstance? Some cosmic joke? Your life is no game, not with a certain set of choices you may choose that lead to an outcome.")
    messagebox.showinfo("Left", "You've been deep into thought so long that it has turned night. You look up into the sky, staring into those deep, empty stars that you know you will never reach." +
                        "You are lost. Not in direction, but life. You are damned to live the rest of your life depressed.")

def right():
    messagebox.showinfo("Right", "You decide to walk the coast. It's actually really peaceful, and you have a lot of time to think. You begin to think about yourself." +
                        " But, just as you begin to get into thought, a giant tiger shark jumps out of the ocean and lands next to you, then eating you violently. You are damned to the digestive tract.")
    messagebox.showinfo("THE END", "THE END")

### Main ###
intro()

root.destroy()     
        


