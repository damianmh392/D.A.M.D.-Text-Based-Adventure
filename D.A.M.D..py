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
                        " fork leads to a large mountain, practicallly untouched by man, and the other" +
                        " to a busy city full of people.")
    approch = simpledialog.askstring("Where Now?","Do you want to go to the City or the Mountian?" +
                                     " (Mountain/City)")
    if approch == "City":
        city()
    elif approch == "Mountain":
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

def yesbeans():
    messagebox.showinfo("Not Just Your Every Day, Ordinary Beans","")

def nobeans():
    messagebox.showinfo("","")
    
def mountains():
    messagebox.showinfo("Mountain","You trek to the mountain and find yourself at home. you decide to live" +
                        " there as a mountain hermit. After several months of living on the mountain, you" +
                        " are approched by Sassquach. The massive creature approches you, it groans and" +
<<<<<<< HEAD
                        " whoops at you, and then waits for a reply")

=======
                        " whoops at you, and then waits for a reply.")
>>>>>>> 64a1b1f0fb934899e5f6179f40655b1484ebbfaa
    reply = simpledialog.askstring("Don't Sass the Quatch","How do you want to resond to Sassquatch's" +
                                   " 'question'. (Whoop/Groan)")
    if reply == "Whoop":
        jacklinks()
    elif reply == "Grunt":
        sassed()                
                        
def jacklinks():
    messagebox.showinfo("You're Bilingual","you make a a big whoop. Sassquatch replys with another whoop and" +
                        " pulls out a bag of Jack Links beef jerky and hands it to you. you take the delicious" +
                        " jerky and Sassquatch renturns to the wilds of the mountain. With a full stomach you" +
                        " continue your life as a hermit and live alone for the rest of your life.")                        
def sassed():                         
    messagebox.showinfo("You Sassed the Squatch","You grunt at Sassquatch. Clearly angered by your reply, he hits" +
                        " you on the head, knocking you out cold. you wake up to see that Sassquatch has taken you home" +
                        " and shows no sign of leaving. forced from your home you perish being unable to find food or"+
                        " shelter.")
    

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
                        " still an oppertunity to turn back. but it is the last chance to do so.")
    
    mtruins = simpledialog.askstring("What is your decision?","you can 'go back', 'mountain', or 'ruins'")
    if mtruins == "go back":
        east()
    elif mtruins == "mountain":
        mountain()
    elif mtruins == "ruins":
        ruins()
    else:
        easternjourney()

def mountain():
    messagebox.showinfo("mountain","you arrived earlier than you must have thought its still light out as the sun sets"+
                         " in front of you, but that cant be right!!? where are you? whats happening! you check"+
                         " behind youand indeed there is another sun there. curiosity flows through your mind as"+
                         " you see this phenomena. you still treck towards the mountain in hopes of finding an "+
                         " ancient secret. or any explanation of this land.")

def ruins():
    messagebox.showinfo("ruins","you arrived earlier than you must have thought its still light out as the sun sets"+
                         " in front of you, but that cant be right!!? where are you? whats happening! you check"+
                         " behind youand indeed there is another sun there. curiosity flows through your mind as"+
                         " you see this phenomena. you still treck towards the ruins in hopes of finding a "+
                         " mighty treasure. or any explanation of this land.")    

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

def sail():
    messagebox.showinfo("Set Sail!","You decide to set sail with the crew. You are treated as a passenger, who really does nothing and eats the sailors' food.")
    messagebox.showinfo("Slavers!", "When you reach the end of your trip, you are ushered off the ship, only to find a man with cages and rope in front of you. " +
                        "There's an exchange of money between the captain and the man, and despite your best efforts, you are bound and put into a cage. " +
                        "You are damned to live the rest of your life as a slave.")
    messagebox. showinfo("THE END", "THE END")

def pirate():
    messagebox.showinfo("Ship", "You step onto the ship, proclaiming that you are now the new captain, and to expel the old leadership. " +
                        "All the sailors look at you funny, and the captain walks out to see the fuss.")
    messagebox.showinfo("Challenge!", "'What do you think you're doing?!' he exclaims. 'Get off my ship!' You stare at him blankly for a few moments, " +
                        "then slap him across the face with a glove, throwing it to the ground.")
    messagebox.showinfo("OOOOH!", "He stands flabbergasted. You take the opportunity to hoist him up onto your shoulders and throw him overboard. " +
                        "He falls to the ocean with a splash. He's immediately eaten by a shark.")
    messagebox.showinfo("New Captain!", "The sailors look at you, stunned, for a moment. Then they break into cheer. " +
                        "'Hail the new captain!' they yell. You give the order to set off to sea.")
    messagebox.showinfo("PIRATES!", "You spend a good five years raiding coastal towns and cities in your new ship with your newfound pirate crew. " +
                        "Unfortunately, one day you contract a sickness, and your second mate, in your weakened state, assumes command and leaves you sickened. " +
                        "You are damned to die of scurvy.")
    messagebox.showinfo("THE END", "THE END")

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
        


