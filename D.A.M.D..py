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
    messagebox.showinfo("","")

def nobeans():
    messagebox.showinfo("","")
    
def mountains():
    messagebox.showinfo("Mountain","You trek to the mountain and find yourself at home. you decide to live" +
                        " there as a mountain hermit. After several months of living on the mountain, you" +
                        " are approched by Sassquach. The massive creature approches you, it groans and" +
                        " whoops at you, and then waits for a reply")
    reply = simpledialog.askstring("Don't Sass the Quatch","How do you want to resond to Sassquatch's" +
                                   " 'question'. (Whoop/Groan)")

    reply = simpledialog.askstring("Don't Sass the Squatch","How do you want to resond to Sassquatch's" +
                                   " 'question'. (Whoop/Grunt)")

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

########################Micah's Functions########################
        
        
def west():
    messagebox.showinfo("West","You have to decided to follow the Western Sunset, leading you to a fork in the road. You have a choice to make: Do you take"
                        " the road less traveled, or the road often traveled? You may also go back to where you woke up and choose a different direction to follow.")
    decision = simpledialog.askstring("Which way do you go?", "Type: 'go back' to go back, 'less traveled' to take the road less traveled, or 'often traveled' to" +
                                      " take the road often traveled.")

    if decision == "go back":
        intro()
    elif decision == "less traveled":
        lesstraveled()
    elif decision == "often traveled":
        oftentraveled()
    else:
        messagebox.showinfo("Incorrect", "That isn't an option.")
        west()
        
def lesstraveled():
    messagebox.showinfo("The road less traveled", "As you head down the far less beaten path, you notice yourself trekking further" +
                        " into a peaceful forest. After hours of hiking, you come across a magnificent cabin! Do you go inside it, or continue walking on" +
                        " the path into the forest? Type 'cabin' to go into the cabin, or 'forest' to keep on walking.")
    
    decision1 = simpledialog.askstring("ASKING", "Type 'forest' to go into the forest, or 'cabin' to enter the cabin.")
    
    if decision1 == "forest":
        forest()

    elif decision1 == "cabin":
        cabin()

def forest():
    messagebox.showinfo("THE FOREST", "You keep on walking through the beautiful woods, and listen to the serene sounds of nature; the sound of" +
                        " squirrels playing with each other, the wind rustling in the trees, and feeling the warm sun on your face. As you listen" +
                        " closely, the sounds start to grow louder... You open your eyes and see a large sign ahead reading 'Beware Rabid Animals!'"+
                        " You turn around to see an army of rabid squirrels heading towards you. You attempt to run, but they throw many acorns" +
                        " at you, causing you to fall down. They amass on your body, and carry you away just like Veruca from Willy Wonka. Except you" +
                        " don't survive. THANKS FOR PLAYING.")

def cabin():
    messagebox.showinfo("THE CABIN", "You approach the large log cabin, which appears to have been untouched for many years. You enter the front door" +
                         ", which is unlocked, and venture into the dark corridors. As you slowly proceed into the kitchen, you hear a raspy voiced man say" +
                         " 'Hello there little one.. Come have dinner with me...' He smiles eerily, and begins walking at you with a knife. You try to" +
                         " run but he is too quick, and caannibalizes you. Curiosity lead to cannibalism. THANKS FOR PLAYING.")


def oftentraveled():
    messagebox.showinfo("The road often traveled", "You take the already beaten and friendly looking path. It looks very artificial and makes the" +
                        " forest feel somewhat more secure. After walking for some time, you come a cross a split path. One way leads to an" +
                        " interestingly empty but sunny freeway, and the other leads to a ghetto city. Which way do you go? Type 'highway' for the" +
                        " highway, or 'city' for the ghetto city.")
    
    decision2 = simpledialog.askstring("ASKING", "Type 'city' to go there, or 'highway' to go there.")
    
    if decision2 == "highway":
        highway()
    elif decision2 == "city":
        city()

def highway():
    messagebox.showinfo("SUNNY HIGHWAY", "You walk into the large, open, sunny freeway. There are almost no cars about on the road, and whatever is there is" +
                        " abandoned. You find a sick Corvette and decide to hotwire it. You get the engine revving, and off you go at high speeds." +
                        " Despite your expert driving skills, a sunglare bounces off the mirror in the car that you were admiring yourself in and" +
                        " blinds you. You veer into the divider and flip over. You were knocked unconcious, but wake up realitively unharmed, the car now" +
                        " upside down. As you attempt to get out, a spill of gasoline is ignited by a sun ray and bursts into flame, engulfing" +
                        " the car, and you, with it. Always wear sunglasses on sunny days. THANKS FOR PLAYING.")

def city():
    messagebox.showinfo("GHETTO CITY", "You swagger into the city, trying to fit in with the local gang members. They don't like that. They promptly mug" +
                        " you and then leave you in the streets, crippled. You eventually get run over by a Mustang playing real life GTA with a" +
                        " friend, who just scored bonus points for hitting a cripple. Never try to walk like a gangster. THANKS FOR PLAYING.")
    

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
        


