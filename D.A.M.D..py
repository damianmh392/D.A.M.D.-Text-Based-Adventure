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
                        " whoops at you, and then waits for a reply.")
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


   

########################Micah's Functions########################
        
        
def west():
    messagebox.showinfo("West","You have to decided to follow the Western Sunset, leading you to a fork in the road. You have a choice to make: Do you take"
                        "the road less traveled, or the road often traveled? You may also go back to where you woke up and choose a different direction to follow.")
    decision = simpledialog.askstring("Which way do you go?", "Type: 'go back' to go back, 'less traveled' to take the road less traveled, or 'often traveled' to take the often"
                                      "the road often traveled.")

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
    decision1 = simpledialog.askstring("The road less traveled", "As you head down the far less beaten path, you notice yourself trekking further" +
                        " into an eerie forest. After hours of hiking, you come across a magnificent cabin! Do you go inside it, or continue walking on" +
                        " the path? Type 'cabin' to go into the cabin, or 'walk' to keep on walking.")

#def cabin():
#def rabidman():
    
#def forest():
#def rabidanimals():

#def oftentraveled():

#def sunnyhighway():
#def sunglare():

#def backroad():
#def getmugged():#



###Deryk's Functions###
def north():
    messagebox.showinfo("","")


### Main ###
intro()

root.destroy()     
        


