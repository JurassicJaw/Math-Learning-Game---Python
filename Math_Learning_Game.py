from tkinter import *
import random
from time import time, sleep
#from PIL import Image, ImageTk
import tkinter as tk
import os
import datetime
import tkinter.messagebox


dict = {"canvas":0}


diff = 0

StoryTimerSeconds = 0
StoryTimer = False

now = datetime.datetime.now()


s = 0
m = 0
h = 0
menuTimer = 4
score = 0
newScore = score
timer = False
Wrong = False
Correct = False
name_grabbed = False
named = False

operator_list = []

operator_list.append("+")
operator_list.append("-")
operator_list.append("*")
operator_list.append("/")

operator = operator_list[random.randint(0,3)]



### csv code made by Vince ###

# Function for reading out of the csv file whichever name you give
# Input: The file name, example: readcsv(TestQuestions.csv)
# Output: a list of all of the items inside the csv
def readcsv(csvname):
  temp_list = [] # Initialize the variable
  dir = os.path.dirname(__file__) # Find the directory of the current file
  filename = os.path.join(dir, 'scores',str(csvname)) # Finds the csv file
  f = open(filename,'r') # opens the csv file
  num_lines = sum(1 for line in open(filename,'r'))
  line = f.readline()  # Skips the header line


  for i in range(1,num_lines): # for every line after that format and append to list
    line = f.readline()
    line = line.rstrip()
    line = line.replace('"','')
    questions = line.split(",")
    # append detials to list #
    temp_list.append(questions)
  f.close() # close the file
  #print(temp_list)
  return temp_list


#Gets the directory of the python file and then goes into the game image folder
#Call the funtion to grab the images (image name goes where it says 'image')
def game_image(image):
  dir = os.path.dirname(__file__) # Gets the path of where the program is
  gameImage = os.path.join(dir, 'images', 'Game' ,str(image)) # Gets the path of where the images are stored.
  img = tk.PhotoImage(file=gameImage)
  return img

#Gets the directory of the python file and then goes into the buttons image folder
#call the function to grab the images (image name goes where it says 'image')
def button_image(image):
  dir = os.path.dirname(__file__) # Gets the path of where the program is
  buttonImage = os.path.join(dir, 'images', 'Buttons' ,str(image)) # Gets the path of where the images are stored.
  img = tk.PhotoImage(file=buttonImage)
  return img





class Game_Questions:


    def Questions():
        global first_number, second_number, first_number_store, second_number_store


        first_number = random.randint(1,50)
        second_number = random.randint(1,50)

        first_number_store = first_number
        second_number_store = second_number 

        if first_number < second_number:
            first_number = second_number_store
            second_number = first_number_store

        question = first_number, operator, second_number
        Game_Questions.Answers()

    def Answers():
        global question, answer, first_number, second_number, first_number_store, second_number_store, randomNumberOne, randomNumberOneStore, randomNumberTwo, randomNumberTwoStore


        if operator == "+":
            answer = first_number + second_number

            AnsPlusRandTen = int(answer) + random.randint(1,10)
            AnsMinusRandTen = int(answer) - random.randint(1,10)

            if AnsMinusRandTen > 0:
                AnsMinusRandTen =  int(answer) - random.randint(1,5)

            randomNumberOne = random.randint(int(answer), int(AnsPlusRandTen))
            randomNumberTwo = random.randint(int(AnsMinusRandTen), int(answer))

            randNumOneBackUp = randomNumberOne
            randNumTwoBackUp = randomNumberTwo


            if randomNumberOne == answer:
                randomNumberOne = randNumOneBackUp
                randomNumberOne = random.randint(AnsMinusRandTen,int(answer))
            
            if randomNumberTwo == answer:
                randomNumberTwo = randNumTwoBackUp
                randomNumberOne = random.randint(int(answer), int(AnsPlusRandTen))


        elif operator == "-":
            answer = first_number - second_number

            if first_number < second_number:
                first_number_store = first_number
                second_number_store = second_number

            AnsPlusRandTen = int(answer) + random.randint(1,10)
            AnsMinusRandTen = int(answer) - random.randint(1,10)

            if AnsMinusRandTen > 0:
                AnsMinusRandTen =  int(answer) - random.randint(1,5)

            randomNumberOne = random.randint(int(answer), int(AnsPlusRandTen))
            randomNumberTwo = random.randint(int(AnsMinusRandTen), int(answer))

            randNumOneBackUp = randomNumberOne
            randNumTwoBackUp = randomNumberTwo

            
            if randomNumberOne == answer:
                randomNumberOne = randNumOneBackUp
                randomNumberOne = random.randint(AnsMinusRandTen,int(answer))
            
            if randomNumberTwo == answer:
                randomNumberTwo = randNumTwoBackUp
                randomNumberOne = random.randint(int(answer), int(AnsPlusRandTen))


        elif operator == "*":
            first_number = random.randint(1,10)
            second_number = random.randint(1,10)

            question = first_number, operator, second_number
            answer = first_number * second_number

            AnsPlusRandTen = int(answer) + random.randint(1,10)
            AnsMinusRandTen = int(answer) - random.randint(1,10)

            if AnsMinusRandTen > 0:
                AnsMinusRandTen =  int(answer) - random.randint(1,5)

            randomNumberOne = random.randint(int(answer), int(AnsPlusRandTen))
            randomNumberTwo = random.randint(int(AnsMinusRandTen), int(answer))

            randNumOneBackUp = randomNumberOne
            randNumTwoBackUp = randomNumberTwo


            if randomNumberOne == answer:
                randomNumberOne = randNumOneBackUp
                randomNumberOne = random.randint(AnsMinusRandTen,int(answer))
            
            if randomNumberTwo == answer:
                randomNumberTwo = randNumTwoBackUp
                randomNumberOne = random.randint(int(answer), int(AnsPlusRandTen))


        elif operator == "/":
            first_number = random.randint(1,10)
            second_number = random.randint(1,10)

            first_number_store = first_number
            second_number_store = second_number

            if first_number < second_number:
                first_number = second_number_store
                second_number = first_number_store


            question = first_number, operator, second_number
            answer = first_number / second_number

            AnsPlusRandTen = int(answer) + random.randint(1,10)
            AnsMinusRandTen = int(answer) - random.randint(1,10)

            if AnsMinusRandTen > 0:
                AnsMinusRandTen =  int(answer) - random.randint(1,5)

            randomNumberOne = random.randint(int(answer), int(AnsPlusRandTen))
            randomNumberTwo = random.randint(int(AnsMinusRandTen), int(answer))

            randNumOneBackUp = randomNumberOne
            randNumTwoBackUp = randomNumberTwo

            if randomNumberOne == answer:
                randomNumberOne = randNumOneBackUp
                randomNumberOne = random.randint(AnsMinusRandTen,int(answer))
            
            if randomNumberTwo == answer:
                randomNumberTwo = randNumTwoBackUp
                randomNumberOne = random.randint(int(answer), int(AnsPlusRandTen))

            if answer.is_integer():
                print("")
            else:
                Game_Questions.Questions()


        Game_Questions.AnswerDisplay()



    def answerOneCheck():
        global answerList, answer, CheckAnswerOne, wrong, Correct, score, diff, CurrentDiff

        if CheckAnswerOne == answer:
            CurrentDiff = diff
            Correct = True
            diff = 0
            score += 1
            Math_Game.StartGame()

        if CheckAnswerOne != answer:
            CurrentDiff = diff
            Wrong = True
            diff = 0
            score -= 1
            Math_Game.StartGame()
    
    def answerTwoCheck():
        global answerList, answer, CheckAnswerTwo, Wrong, Correct, score, diff, CurrentDiff

        if CheckAnswerTwo == answer:
            CurrentDiff = diff
            Correct = True
            diff = 0
            score += 1
            Math_Game.StartGame()

        if CheckAnswerTwo != answer:
            CurrentDiff = diff
            Wrong = True
            diff = 0
            score -= 1
            Math_Game.StartGame()


    def AnswerDisplay():
        global question, answer, randomNumberOne, randomNumberTwo, operator, CheckAnswerOne, CheckAnswerTwo

        dict["canvas"] = canvas
        canvas.delete('all')

        score = 0

        question = first_number, operator, second_number

        

        answerList = []


        answerList.append(int(answer))
        answerList.append(int(randomNumberOne))
        answerList.append(int(randomNumberTwo))

        randomListOne = answerList[random.randint(0,2)]
        randomListTwo = answerList[random.randint(0,2)]


        AnswerOneText = answerList.pop(random.randint(0,2))
        AnswerTwoText = answerList.pop(random.randint(0,1))

        CheckAnswerOne = AnswerOneText
        CheckAnswerTwo = AnswerTwoText

        BackImages = [game_image('Game#1.ppm'), game_image('Game#2.ppm'),game_image('Game#3.ppm')]

        RandomLevel = BackImages[random.randint(0,2)]

        #Importing the image onto the canvas
        BackGround = RandomLevel
        BackGround = BackGround.subsample(3)
        CavnasImage = Label(root, image = BackGround)
        CavnasImage.place(x = 0, y = 0)


        if RandomLevel == BackImages[0]:
            dict["canvas"] = canvas
            canvas.delete('all')


            #Makes Buttons
            answerOne = Button(root,text=AnswerOneText,font="Times 18 bold",width = 7, height = 1, bg = 'lightcyan4', highlightthickness = 0, bd = 0, command=Game_Questions.answerOneCheck)
            CheckAnswerOne

            answerTwo = Button(root,text=AnswerTwoText,font="Times 18 bold",width = 7, height = 1, bg = 'lightcyan4', highlightthickness = 0, bd = 0, command=Game_Questions.answerTwoCheck)
            CheckAnswerTwo

            PickRandom = [answerOne, answerTwo]
            PickRandomText = [AnswerOneText, AnswerTwoText]

            #Creating the buttons
            menuButton = button_image('Back.ppm')
            menuButton = menuButton.subsample(3)
            Menu = Button(root,text="",image=menuButton,highlightthickness=0,bd=0,command=Math_Game.Main_Menu)

            Menu_canvas = canvas.create_window( 610, 700, anchor = "nw",window = Menu)

            #ANSWER List = ANSWER
            if AnswerOneText != int(answer) and AnswerTwoText != int(answer):

                RandomPick = random.choice(PickRandom)

                if RandomPick == answerOne:
                    AnswerOneText = answer
                    answerOne.config(text=int(AnswerOneText))
                    CheckAnswerOne = answer

                elif RandomPick == answerTwo:
                    AnswerTwoText = answer
                    answerTwo.config(text=int(AnswerTwoText))
                    CheckAnswerTwo = answer
        

            operator = operator_list[random.randint(0,3)]

            #Displays the buttons
            answerOne_canvas = canvas.create_window( 75, 175, anchor = "nw",window = answerOne)
            answerTwo_canvas = canvas.create_window( 635, 175, anchor = "nw",window = answerTwo)

            #Makes the Question Label
            question_label = Label(root, text = question, font="Times 35 bold",width = 7, height = 1, bg = 'slategray3')
            question_label.place(x=325,y=720)
    
        elif RandomLevel == BackImages[1]:
            dict["canvas"] = canvas
            canvas.delete('all')

            #Makes Buttons
            answerOne = Button(root,text=AnswerOneText,font="Times 18 bold",width = 7, height = 1, bg = 'lightcyan4', highlightthickness = 0, bd = 0, command=Game_Questions.answerOneCheck)
            CheckAnswerOne

            answerTwo = Button(root,text=AnswerTwoText,font="Times 18 bold",width = 7, height = 1, bg = 'lightcyan4', highlightthickness = 0, bd = 0, command=Game_Questions.answerTwoCheck)
            CheckAnswerTwo

            PickRandom = [answerOne, answerTwo]
            PickRandomText = [AnswerOneText, AnswerTwoText]

            #Creating the buttons
            menuButton = button_image('Back.ppm')
            menuButton = menuButton.subsample(3)
            Menu = Button(root,text="",image=menuButton,highlightthickness=0,bd=0,command=Math_Game.Main_Menu)

            Menu_canvas = canvas.create_window( 610, 700, anchor = "nw",window = Menu)

            #ANSWER List = ANSWER
            if AnswerOneText != int(answer) and AnswerTwoText != int(answer):

                RandomPick = random.choice(PickRandom)

                if RandomPick == answerOne:
                    AnswerOneText = answer
                    answerOne.config(text=int(AnswerOneText))
                    CheckAnswerOne = answer

                elif RandomPick == answerTwo:
                    AnswerTwoText = answer
                    answerTwo.config(text=int(AnswerTwoText))
                    CheckAnswerTwo = answer
            

            operator = operator_list[random.randint(0,3)]

            #Displays the buttons
            answerOne_canvas = canvas.create_window( 100, 250, anchor = "nw",window = answerOne)
            answerTwo_canvas = canvas.create_window( 600, 250, anchor = "nw",window = answerTwo)

            #Makes the Question Label
            question_label = Label(root, text = question, font="Times 35 bold",width = 7, height = 1, bg = 'slategray3')
            question_label.place(x=325,y=720)

        elif RandomLevel == BackImages[2]:
            dict["canvas"] = canvas
            canvas.delete('all')
            
            #Makes Buttons
            answerOne = Button(root,text=AnswerOneText,font="Times 18 bold",width = 7, height = 1, bg = 'lightcyan4', highlightthickness = 0, bd = 0, command=Game_Questions.answerOneCheck)
            CheckAnswerOne

            answerTwo = Button(root,text=AnswerTwoText,font="Times 18 bold",width = 7, height = 1, bg = 'lightcyan4', highlightthickness = 0, bd = 0, command=Game_Questions.answerTwoCheck)
            CheckAnswerTwo

            PickRandom = [answerOne, answerTwo]
            PickRandomText = [AnswerOneText, AnswerTwoText]

            #Creating the buttons
            menuButton = button_image('Back.ppm')
            menuButton = menuButton.subsample(3)
            Menu = Button(root,text="",image=menuButton,highlightthickness=0,bd=0,command=Math_Game.Main_Menu)

            Menu_canvas = canvas.create_window( 610, 700, anchor = "nw",window = Menu)

            #ANSWER List = ANSWER
            if AnswerOneText != int(answer) and AnswerTwoText != int(answer):

                RandomPick = random.choice(PickRandom)

                if RandomPick == answerOne:
                    AnswerOneText = answer
                    answerOne.config(text=int(AnswerOneText))
                    CheckAnswerOne = answer

                elif RandomPick == answerTwo:
                    AnswerTwoText = answer
                    answerTwo.config(text=int(AnswerTwoText))
                    CheckAnswerTwo = answer
            
            

            operator = operator_list[random.randint(0,3)]

            #Displays the buttons
            answerOne_canvas = canvas.create_window( 125, 50, anchor = "nw",window = answerOne)
            answerTwo_canvas = canvas.create_window( 680, 200, anchor = "nw",window = answerTwo)

            #Makes the Question Label
            question_label = Label(root, text = question, font="Times 35 bold",width = 7, height = 1, bg = 'slategray3')
            question_label.place(x=325,y=720)


        dict["canvas"].pack()
        root.mainloop()



class Math_Game:

    def Exit():                 #Quits The Game
        root.destroy()


    def Main_Menu():            #Loads Up The Main Menu
        global CanvasImage, BackGround, timer, name

        dict["canvas"] = canvas
        canvas.delete('all')

        timer = False

        #Importing the image onto the canvas
        BackGround = game_image('StartMenu.ppm')
        BackGround = BackGround.subsample(3)
        CavnasImage = Label(root, image = BackGround)
        CavnasImage.place(x = 0, y = 0)


        #Creating the buttons
        StartButton = button_image('Start.ppm')
        StartButton = StartButton.subsample(3)
        Start = Button(root, text = "", image = StartButton, highlightthickness = 0, bd = 0, command=Math_Game.Difficulty_Menu)

        HighScoresButton = button_image('Highscores.ppm')
        HighScoresButton = HighScoresButton.subsample(3)
        HighScores = Button(root, text = "", image = HighScoresButton, highlightthickness = 0, bd = 0,command=scoreInfo)

        QuitButton = button_image('Quit.ppm')
        QuitButton = QuitButton.subsample(3)
        Quit = Button(root, text = "", image = QuitButton, highlightthickness = 0, bd = 0,command=Math_Game.Exit)


        #Displaying the buttons
        Start_canvas = canvas.create_window( 300, 400, anchor = "nw",window = Start)
        HighScore_canvas = canvas.create_window( 215, 500, anchor = "nw",window = HighScores)
        Quit_canvas = canvas.create_window( 315, 600, anchor = "nw",window = Quit)

        dict["canvas"].pack()
        if named == False:
            Math_Game.NamePopUp()
        root.mainloop()   


    
    def NamePopUp():
        global NameEntry, Name_Var, named
        
        
        named = True
        canvas = Canvas(PopUp, width=300, height=150, bg = 'grey25')
    

        #Makes The Entry Box And Displays It
        NameEntry = Entry(PopUp, width=25,font='Times 20 bold',justify='center')
        NameEntry.place(x=77,y=50, width=151, height=40)

        #Makes the text above the entry box and displays it
        label = Label(PopUp, text="-- Enter A Name --", bg='grey25', fg='azure', font="Times 15 bold")
        canvas.create_window(152, 25, window=label)

        #Makes the confirm button for the name and displays it onto the canvas
        NameButton = Button(PopUp, text='Confirm Name', font='Times 15 bold', command=Math_Game.nameValidate)
        canvas.create_window(152,125, window=NameButton)


        canvas.pack()

    def nameValidate():
        global name_grabbed, name

        if len(NameEntry.get()) == 0:
            
            def closeError():
                ErrorRoot.destroy()

            ErrorRoot = Tk()
            ErrorRoot.title("Error!")
            ErrorRoot.attributes("-topmost", 3)
            

            canvas = Canvas(ErrorRoot, width=200, height=75)

            errormessage = Label(ErrorRoot, text="Please Enter A Name!", font='Times 13 bold')
            canvas.create_window(100, 37, window=errormessage)
            errormessage.after(2000, closeError)

            canvas.pack()

        else:
            root.attributes("-topmost", 1)
            name_grabbed = True
            name=NameEntry.get()
            PopUp.destroy()



    def Difficulty_Menu():      #Loads Up The DIfficulty Menu
        global CanvasImage, BackGround

        dict["canvas"] = canvas
        canvas.delete('all')

        #Importing the image onto the canvas
        BackGround = game_image('Difficulty.ppm')
        BackGround = BackGround.subsample(3)
        CavnasImage = Label(root, image = BackGround)
        CavnasImage.place(x = 0, y = 0)


        #Creating the buttons
        EasyButton = button_image('Easy.ppm')
        EasyButton = EasyButton.subsample(3)
        Easy = Button(root,text="",image=EasyButton,highlightthickness=0,bd=0,command=Math_Game.EasyToggle)

        MediumButton = button_image('Medium.ppm')
        MediumButton = MediumButton.subsample(3)
        Medium = Button(root,text="",image=MediumButton,highlightthickness=0,bd=0,command=Math_Game.MediumToggle)

        HardButton = button_image('Hard.ppm')
        HardButton = HardButton.subsample(3)
        Hard = Button(root,text="",image=HardButton,highlightthickness=0,bd=0,command=Math_Game.HardToggle)


        #Displaying the buttons
        Easy_canvas = canvas.create_window( 300, 400, anchor = "nw",window = Easy)
        Medium_canvas = canvas.create_window( 255, 500, anchor = "nw",window = Medium)
        Hard_canvas = canvas.create_window( 300, 600, anchor = "nw",window = Hard)

        #Menu Button
        menuButton = button_image('Back.ppm')
        menuButton = menuButton.subsample(3)
        Menu = Button(root,text="",image=menuButton,highlightthickness=0,bd=0,command=Math_Game.Main_Menu)

        Menu_canvas = canvas.create_window( 610, 700, anchor = "nw",window = Menu)



        dict["canvas"].pack()
        root.mainloop()


    def Timer():               #Starts And Stops The Timer
        global s,m,h,timer,timer_label,time_count,BackGround,CavnasImage, score, menuTimer, newScore, diff, CurrentDiff

        #Makes the timer label
        timer_label = Label(root, text=" ", font=('Helvetica', 24), fg='black')

        if timer == True:

            time_count = h,":", m,":", s

            #Displays the timer on the canvas
            timer_canvas = canvas.create_window( 663, 10, anchor = "nw",window = timer_label)
            

            #Updates the timer label
            timer_label.configure(text=time_count)


            #Minus 1 Every Second
            s -= 1

            #Seconds To Minutes
            if s > 59:
                s -=59
                m += 1
            
            #Minutes To Seconds
            if m > 0 and s < 0:
                m-=1
                s+=60
            
            #Minutes To Hours
            if m > 60 and s > 0:
                s=0
                m =0
                h +=1

            #Hours To Minutes
            if h > 0 and m < 1 and s < 0:
                h -= 1
                m += 59
                s = 59

            #No Time Left
            elif s < 0:
                s=0
                
                BackGround = game_image('GameOver.ppm')
                BackGround = BackGround.subsample(3)
                CavnasImage = Label(root, image = BackGround)
                CavnasImage.place(x = 0, y = 0)

                finalScore = "Score: %d" % int(score)
            
                ScoreText = Label(root, text=finalScore, font=('Helvetica', 24), fg='black')
                Score_Window = canvas.create_window( 335, 600, anchor = "nw",window = ScoreText)

                newScore = score

                menuTimer -=1

                if menuTimer < 0:
                    timer=False
                    ScoreText.destroy
                    
                    print("Current Diff:" CurrentDiff)
                    if CurrentDiff == 1:

                        print("APPENDING SCORE TO THE CSV FILE")
                        dir = os.path.dirname(__file__) # Find the directory of the current file
                        filename = os.path.join(dir, 'scores',str('Easy.csv').lower()) # Finds the csv file
                        f = open(filename,'a') # opens the csv file

                        f.write("\n" + str(name) + ": " + str(score))
                        f.close() # close the file
                        
                
                    elif CurrentDiff == 2:

                        print("APPENDING SCORE TO THE CSV FILE")
                        dir = os.path.dirname(__file__) # Find the directory of the current file
                        filename = os.path.join(dir, 'scores',str('Medium.csv').lower()) # Finds the csv file
                        f = open(filename,'a') # opens the csv file

                        f.write("\n" + str(name) + ": " + str(score))
                        f.close() # close the file
                        

                    elif CurrentDiff == 3:

                        print("APPENDING SCORE TO THE CSV FILE")
                        dir = os.path.dirname(__file__) # Find the directory of the current file
                        filename = os.path.join(dir, 'scores',str('Hard.csv').lower()) # Finds the csv file
                        f = open(filename,'a') # opens the csv file

                        f.write("\n" + str(name) + ": " + str(score))
                        f.close() # close the file
                        

                        

                    Math_Game.Main_Menu()
                
                root.after(1000, Math_Game.Timer)


            #Loop
            root.after(1000, Math_Game.Timer)


        #Sets everything to 0 when False
        elif timer == False:
            s = 0
            m = 0
            h = 0

            #Sets the timer to blank
            timer_label.configure(text=" ")


    def TimerOn():             #Turns The Timmer On
        global timer
        timer = True


    def TimerOff():            #Turns The Timer Off
        global timer
        timer = False


    def StoryMenu():            #Loads Up The Story Menu
        global StoryTimer, StoryTimerSeconds
        dict["canvas"] = canvas
        canvas.delete('all')
        StoryTimer = True

        #Importing the image onto the canvas
        BackGround = game_image('Story.ppm')
        BackGround = BackGround.subsample(3)
        CavnasImage = Label(root, image = BackGround)
        CavnasImage.place(x = 0, y = 0)

        Math_Game.TimerStory()

        dict["canvas"].pack()
        root.mainloop()


    def TimerStory():           #Starts The Timer For The Story Menu
        global StoryTimerSeconds, StoryTimer

        if StoryTimer == True:

            StoryTimerSeconds += 1

            if StoryTimerSeconds == 3:
                StoryTimerSeconds = 0
                Math_Game.StartGame()

            root.after(1000, Math_Game.TimerStory)


    def EasyToggle():           #Toggles Easy Mode
        global diff
        diff = 1

        Math_Game.StoryMenu()


    def MediumToggle():         #Toggles Medium Mode
        global diff
        diff = 2

        Math_Game.StoryMenu()


    def HardToggle():           #Toggles Hard Mode
        global diff
        diff = 3

        Math_Game.StoryMenu()


    def StartGame():           #Starts The Game
        global diff, h, m, s, score, timer, timer_label, answers, Correct, Wrong, time_count

        if diff == 1:
            s = 31
            m = 0
            h = 0
            Math_Game.TimerOn()
            Math_Game.Timer()

        elif diff == 2:
            s = 21
            m = 0
            h = 0
            Math_Game.TimerOn()
            Math_Game.Timer()

        elif diff == 3:
            s = 11
            m = 0
            h = 0
            Math_Game.TimerOn()
            Math_Game.Timer()


        if Correct == True:
            s += 5
            time_count = h,":", m,":", s
            timer_label.configure(text="")
            timer_label.configure(text=time_count)
            Correct = False
            if s > 59:
                s -=59
                m += 1
                timer_label.configure(text="")
                timer_label.configure(text=time_count)
            

        if Wrong == True:
            s -=10
            time_count = h,":", m,":", s
            timer_label.configure(text="")
            timer_label.configure(text=time_count)
            Wrong = False
            if m > 0 and s < 0:
                m-=1
                s+=60
                timer_label.configure(text="")
                timer_label.configure(text=time_count)


        Game_Questions.Questions()



def scoreInfo():
    tkinter.messagebox.showinfo(title="Scores",message="Scores are located inside the scores folder.\nAs I could'y get it to work here.")


def on_closing():
    PopUp.destroy()
    if name_grabbed == False:
        root.destroy()


def disable_event():
    pass

def Alarm(event):
        PopUp.focus_force()
        PopUp.bell()
        

root=Tk()
root.title("Math Game")
root.protocol("WM_DELETE_WINDOW", disable_event)

PopUp = Tk()
PopUp.title(" -=- Please Enter A Name -=- ")
PopUp.bind("<FocusOut>", Alarm)
PopUp.protocol("WM_DELETE_WINDOW", on_closing)
PopUp.attributes("-topmost", 2)

canvas = Canvas(root,width=800,height=800)

Math_Game.Main_Menu()

