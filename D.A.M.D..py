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
    messagebox.showinfo("","")

def nobeans():
    messagebox.showinfo("","")
    
def mountains():
    messagebox.showinfo("Mountain","You trek to the mountain and find yourself at home. you decide to live" +
                        " there as a mountain hermit. After several months of living on the mountain, you" +
                        " are approched by Sassquach. The massive creature approches you, it groans and" +
                        " whoops at you, and then waits for a reply")
<<<<<<< HEAD
    reply = simpledialog.askstring("Don't Sass the Quatch","How do you want to resond to Sassquatch's" +
                                   " 'question'. (Whoop/Groan)")
=======
    reply = simpledialog.askstring("Don't Sass the Squatch","How do you want to resond to Sassquatch's" +
                                   " 'question'. (Whoop/Grunt)")
>>>>>>> 7766ffa26cdbf3a697ee69e4b2da4ab877450bd2
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
def north():
    messagebox.showinfo("","")


### Main ###
intro()

root.destroy()     
        


