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
    messagebox.showinfo("The Crossroads","You wake up in a four way intersection. There are small dirt" +
                        " paths in a field, one going North, one South, one East, and one West. Which" +
                        " path do you wish to choose?")
    path = simpledialog.askstring("Where to Go","Type the direction you wish to go, choose your path. Your options are ''North, South, East, and West''")
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

def intro2():
    messagebox.showinfo("The Crossroads","There are small dirt" +
                        " paths in a field, one going North, one South, one East, and one West. Which" +
                        " path do you wish to choose?")
    path = simpledialog.askstring("Where to Go","Type the direction you wish to go, choose your path. Your options are ''North, South, East, and West''")
    if path == "North":
        north()

    elif path == "South":
        south()

    elif path == "East":
        east()

    elif path == "West":
        west()

    else:
        intro2()        


###Damian's Functions###
def south():
    messagebox.showinfo("South","You have headed down the South path and arive at a fork in the road. One" +
                        " fork leads to a large mountain, practically untouched by man, and the other" +
                        " to a busy city full of people.")
    approch = simpledialog.askstring("Where Now?","Do you want to go to the City, the Mountian? Or would you want to go back" +
                                     " (Mountain/City/Back)")
    if approch == "City":
        city()
    elif approch == "Mountain":
        mountains()
    elif approch == "Back":
        intro2()    
    else:
        south()

def city():
    messagebox.showinfo("City","You walk into the bustling city and shortly after a hobo aproches you." +
                        " This decrepid man in tattered clothes askes you ''You! Do you want some beans?" +
                        " They're great, I guarantee they're quality beans!''")
    beans = simpledialog.askstring("Beans?","Do you accept the hobo's beans? (Yes/No)")
    if beans == "Yes":
        yesbeans()
    elif beans == "No":
        nobeans()
    else:
        city()        

def yesbeans():
    messagebox.showinfo("Not Just Your Every Day, Ordinary Beans","You take the hobo's beans and crack the can open with" +
                        " an opener he lends you. Quickly after you eat the beans, you feel a funny sensation. You look down to" +
                        " see that you seemingly are fading from reality and promptly blackout. You awaken to see a completely" +
                        " different city beneath you feet. The buildings are ragged and old and the streets filled with" +
                        " hobos. You've unknowingly transported yourself to the lost city of Hobotopolis. You decide that" +
                        " since you are there you should live in the great metropolis as a hobo yourself. After you settle" +
                        " in Hobotopolis you live you life as a profesional hobo.")

def nobeans():
    messagebox.showinfo("That's Not A Can Opener","Clearly offended and angered by your rejection of his can of beans," +
                        " the hobo pulls a knife on you and mugs you for all your money. After finding out you have no" +
                        " no such thing you both share a greatly awkward moment of silence before he dashes into a nearby" +
                        " alley never to be seen again. You soon settle in the city and live a long and ok life.")
    
def mountains():
    messagebox.showinfo("Mountain","You trek to the mountain and find yourself at home. You decide to live" +
                        " there as a mountain hermit. After several months of living on the mountain, you" +
                        " are approched by Sassquach. The massive creature, soon after it approching you," +
                        " grunts and whoops at you, and then waits for a reply.")
    reply = simpledialog.askstring("Don't Sass the Squatch","How do you want to resond to Sassquatch's" +
                                   " 'question'. (Whoop/Grunt)")
    if reply == "Whoop":
        jacklinks()
    elif reply == "Grunt":
        sassed()                
                        
def jacklinks():
    messagebox.showinfo("You're Bilingual!","You make a big whoop. Sassquatch replys with another whoop and" +
                        " pulls out a bag of Jack Links beef jerky and hands it to you. You take the delicious" +
                        " jerky and Sassquatch renturns to the wilds of the mountain. With a full stomach you" +
                        " continue your life as a hermit and live alone for the rest of your life.")                        
def sassed():                         
    messagebox.showinfo("You Sassed the Squatch","You grunt at Sassquatch. Clearly angered by your reply, he hits" +
                        " you on the head, knocking you out cold. You wake up to see that Sassquatch has taken you home" +
                        " and shows no sign of leaving. Forced from your home you perish being unable to find food or"+
                        " shelter.")
    

###Andrew's Functions###
#lets start how to do this thing#
def east():
    messagebox.showinfo("East"," Your journey begins as of now. Yet there is still yet a chance"+
                        " to turn back, if you so choose but only a coward turns back from any"+
                        " adventure presented to him." )
    goback = simpledialog.askstring("turn back?"," Do you desire a different path?")
    if goback == "yes":
        intro2()
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

########################Micah's Functions########################
        
        
def west():
    messagebox.showinfo("West","You have to decided to follow the Western Sunset, leading you to a fork in the road. You have a choice to make: Do you take"
                        "the road less traveled, or the road often traveled? You may also go back to where you woke up and choose a different direction to follow.")
    decision = simpledialog.askstring("Which way do you go?", "Type: 'go back' to go back, 'less traveled' to take the road less traveled, or 'often traveled' to take the often"
                                      "the road often traveled.")

    if decision == "go back":
        intro2()
    elif decision == "less traveled":
        lesstraveled()
    elif decision == "often traveled":
        oftentraveled()
    else:
        messagebox.showinfo("Incorrect", "That isn't an option.")
        west()
        
def lesstraveled():
    decision1 = simpledialog.askstring("The road less traveled", "As you head down the far less beaten path, you notice yourself trekking further" +
                        " into a peaceful forest. After hours of hiking, you come across a magnificent cabin! Do you go inside it, or continue walking on" +
                        " the path? Type 'cabin' to go into the cabin, or 'walk' to keep on walking.")
    if decision1 == cabin:
        cabin()
    elif decision1 == walk:
        forest()
    else:
        messagebox.showinfo("Nope", "There's nothing else to do, please choose one of the available options.")
        lesstraveled()


def cabin():
    messagebox.showinfo("THE CABIN", "You push your way into the large cabin door, and it is silent as you work it open. The" +
                        " room is large, and dimly lit with natural light. It is decorated with typical cabin decor, and many animal heads" +
                        ". You make your way into the kitchen, trying not to stumble, when you hear a raspy voice come from behind:" +
                        " 'Would you like to join me for dinner?' You turn around to see a burly man with a raggedy head of hair and a" +
                        " dark, thick beard. He approaches you with a knife.")
    dinner = simpledialog.askstring("What do you do?", "Type 'yes' to join the man in dinner, or 'no' to run out of the house.")
        if dinner == "yes":
            dinnerdeath()
        elif dinner == "no":
            dinnerlive()

def dinnerdeath():
    messagebox.showinfo("Time for dinner", "You happily say yes, and the man smiles eerily. He grabs you and pulls you" +
                        " into the kitchen where he proceeds to murder you, and incorporates you into his dinner. Curiosity lead to" +
                        " cannibalism.. THANKS FOR PLAYING.")
def dinnerlive():
    messagebox.showinfo("Time to run", "You 
#def forest():
#def rabidanimals():

#def oftentraveled():

#def sunnyhighway():
#def sunglare():

#def backroad():
#def getmugged():#



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
        intro2()
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
        


