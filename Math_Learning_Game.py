from tkinter import *
import random
import time
from PIL import Image, ImageTk
import tkinter as tk

dict = {"canvas":0}

BackImages = ["G:\My Drive\Classroom\CDT301\Python Assesment\Math Learning Game\Layouts\Images\Menus\PPM\StartMenu.ppm",   # StartMenu (0)
            "G:\My Drive\Classroom\CDT301\Python Assesment\Math Learning Game\Layouts\Images\Menus\PPM\Difficulty.ppm",    # Difficulty (1)
            "G:\My Drive\Classroom\CDT301\Python Assesment\Math Learning Game\Layouts\Images\Menus\PPM\Story.ppm",         # Story (2)
            "G:\My Drive\Classroom\CDT301\Python Assesment\Math Learning Game\Layouts\Images\Game\PPM\Game#1.ppm",         # Game#1 (3)
            "G:\My Drive\Classroom\CDT301\Python Assesment\Math Learning Game\Layouts\Images\Game\PPM\Game#2.ppm",         # Game#2 (4)
            "G:\My Drive\Classroom\CDT301\Python Assesment\Math Learning Game\Layouts\Images\Game\PPM\Game#3.ppm"]         # Game3 (5)

ButtonImages = ["G:\My Drive\Classroom\CDT301\Python Assesment\Math Learning Game\Layouts\Images\Buttons\PPM\Back.ppm",          # Back (0)
                "G:\My Drive\Classroom\CDT301\Python Assesment\Math Learning Game\Layouts\Images\Buttons\PPM\Easy.ppm",          # Easy (1)
                "G:\My Drive\Classroom\CDT301\Python Assesment\Math Learning Game\Layouts\Images\Buttons\PPM\Medium.ppm",        # Medium (2)
                "G:\My Drive\Classroom\CDT301\Python Assesment\Math Learning Game\Layouts\Images\Buttons\PPM\Hard.ppm",          # Hard (3)
                "G:\My Drive\Classroom\CDT301\Python Assesment\Math Learning Game\Layouts\Images\Buttons\PPM\Highscores.ppm",    # Highscores (4)
                "G:\My Drive\Classroom\CDT301\Python Assesment\Math Learning Game\Layouts\Images\Buttons\PPM\Quit.ppm",          # Quit (5)
                "G:\My Drive\Classroom\CDT301\Python Assesment\Math Learning Game\Layouts\Images\Buttons\PPM\Ready.ppm",         # Ready (6)
                "G:\My Drive\Classroom\CDT301\Python Assesment\Math Learning Game\Layouts\Images\Buttons\PPM\Start.ppm",         # Start (7)
                "G:\My Drive\Classroom\CDT301\Python Assesment\Math Learning Game\Layouts\Images\Buttons\PNG\Title.png",         # Title (8)
                "G:\My Drive\Classroom\CDT301\Python Assesment\Math Learning Game\Layouts\Images\GameOver\PPM\GameOver.ppm"]     # Game Over (9)


EasyDiff = 0
MediumDiff = 0
HardDiff = 0

StoryTimerSeconds = 0
StoryTimer = False

s = 0
m = 0
h = 0
score = 0
timer = False











class Math_Game:

    def Exit():                 #Quits The Game
        root.destroy()


    def HighScoreMenu():        #Loads Up The Main Menu
        print("HighScores!")


    def Main_Menu():            #Loads Up The Main Menu
        global CanvasImage, BackGround, BackImages, BackImages

        dict["canvas"] = canvas
        canvas.delete('all')

        #Importing the image onto the canvas
        BackGround = PhotoImage(file = BackImages[0])
        BackGround = BackGround.subsample(3)
        CavnasImage = Label(root, image = BackGround)
        CavnasImage.place(x = 0, y = 0)


        #Creating the buttons
        StartButton = PhotoImage(file = ButtonImages[7])
        StartButton = StartButton.subsample(3)
        Start = Button(root, text = "", image = StartButton, highlightthickness = 0, bd = 0, command=Math_Game.Difficulty_Menu)

        HighScoresButton = PhotoImage(file = ButtonImages[4])
        HighScoresButton = HighScoresButton.subsample(3)
        HighScores = Button(root, text = "", image = HighScoresButton, highlightthickness = 0, bd = 0,command=Math_Game.HighScoreMenu)

        QuitButton = PhotoImage(file = ButtonImages[5])
        QuitButton = QuitButton.subsample(3)
        Quit = Button(root, text = "", image = QuitButton, highlightthickness = 0, bd = 0,command=Math_Game.Exit)


        #Displaying the buttons
        Start_canvas = canvas.create_window( 300, 400, anchor = "nw",window = Start)
        HighScore_canvas = canvas.create_window( 215, 500, anchor = "nw",window = HighScores)
        Quit_canvas = canvas.create_window( 315, 600, anchor = "nw",window = Quit)
        



        
        dict["canvas"].pack()
        root.mainloop()


    def Difficulty_Menu():      #Loads Up The DIfficulty Menu
        global CanvasImage, BackGround, BackImages, BackImages

        dict["canvas"] = canvas
        canvas.delete('all')

        #Importing the image onto the canvas
        BackGround = PhotoImage(file = BackImages[1])
        BackGround = BackGround.subsample(3)
        CavnasImage = Label(root, image = BackGround)
        CavnasImage.place(x = 0, y = 0)


        #Creating the buttons
        EasyButton = PhotoImage(file = ButtonImages[1])
        EasyButton = EasyButton.subsample(3)
        Easy = Button(root,text="",image=EasyButton,highlightthickness=0,bd=0,command=Math_Game.EasyToggle)

        MediumButton = PhotoImage(file = ButtonImages[2])
        MediumButton = MediumButton.subsample(3)
        Medium = Button(root,text="",image=MediumButton,highlightthickness=0,bd=0,command=Math_Game.MediumToggle)

        HardButton = PhotoImage(file = ButtonImages[3])
        HardButton = HardButton.subsample(3)
        Hard = Button(root,text="",image=HardButton,highlightthickness=0,bd=0,command=Math_Game.HardToggle)


        #Displaying the buttons
        Easy_canvas = canvas.create_window( 300, 400, anchor = "nw",window = Easy)
        Medium_canvas = canvas.create_window( 255, 500, anchor = "nw",window = Medium)
        Hard_canvas = canvas.create_window( 300, 600, anchor = "nw",window = Hard)



        dict["canvas"].pack()
        root.mainloop()


    def StoryMenu():            #Loads Up The Story Menu
        global StoryTimer, StoryTimerSeconds
        dict["canvas"] = canvas
        canvas.delete('all')
        StoryTimer = True

        #Importing the image onto the canvas
        BackGround = PhotoImage(file = BackImages[2])
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
                Math_Game.StartGame()

            root.after(1000, Math_Game.TimerStory)

        elif StoryTimer == False:
            s = 0
            m = 0
            h = 0
            print(h,m,s)


    def EasyToggle():           #Toggles Easy Mode
        global EasyDiff, MediumDiff, HardDiff
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
        global diff, h, m, s, score, timer, timer_label, answers

        if diff == 1:
            s = 31
            m = 2
            h = 0
            Math_Game.TimerOn()
            Math_Game.Timer()

        elif diff == 2:
            s = 46
            m = 1
            h = 0
            Math_Game.TimerOn()
            Math_Game.Timer()

        elif diff == 3:
            s = 1
            m = 1
            h = 0
            Math_Game.TimerOn()
            Math_Game.Timer()

        dict["canvas"] = canvas
        canvas.delete('all')

        #Importing the image onto the canvas
        BackGround = PhotoImage(file = BackImages[random.randint(3,5)])
        BackGround = BackGround.subsample(3)
        CavnasImage = Label(root, image = BackGround)
        CavnasImage.place(x = 0, y = 0)


        #Creating the buttons
        QuitButton = PhotoImage(file = ButtonImages[5])
        QuitButton = QuitButton.subsample(4)
        Quit = Button(root, text = "", image = QuitButton, highlightthickness = 0, bd = 0, command=Math_Game.Exit)



        #Displays the buttons
        Quit_canvas = canvas.create_window( 663, 727, anchor = "nw",window = Quit)





        Game_Questions.Questions()

        dict["canvas"].pack()
        root.mainloop()


    def Timer():               #Starts And Stops The Timer
        global s,m,h,timer,timer_label,time_count,BackGround,CavnasImage,BackImages

        if timer == True:

            time_count = h,":", m,":", s

            #Displays the timer on the canvas
            timer_label = Label(root, text=" ", font=('Helvetica', 24), fg='black')
            timer_canvas = canvas.create_window( 663, 10, anchor = "nw",window = timer_label)

            #Updates the timer label
            timer_label.configure(text=time_count)


            #Minus 1 Every Second
            s -= 1

            #Seconds To Minutes
            if s > 59:
                s=0
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
                timer=False
                BackGround = PhotoImage(file = BackImages[9])
                BackGround = BackGround.subsample(3)
                CavnasImage = Label(root, image = BackGround)
                CavnasImage.place(x = 0, y = 0)


            #Loop
            root.after(1000, Math_Game.Timer)


        #Sets everything to 0 when False
        elif timer == False:
            s = 0
            m = 0
            h = 0
            print("Stopped")

            #Sets the timer to blank
            timer_label.configure(text=" ")

            print("Your score is ", score)


    def CorrectAnswer():       #Gives Time If You Get It Correct
        global s,m,h,timer,score

        s += 10
        score +=10

        #Updates the timer label
        timer_label.configure(text=time_count)


        #Minus 1 Every Second
        s -= 1

        #Seconds To Minutes
        if s > 59:
            s=0
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
            timer=False
            BackGround = PhotoImage(file = BackImages[9])
            BackGround = BackGround.subsample(3)
            CavnasImage = Label(root, image = BackGround)
            CavnasImage.place(x = 0, y = 0)


    def WrongAnswer():         #Removes Time If You Get It Wrong
        global s,m,h,timer,score

        s -= 10
        score -= 10

        #Updates the timer label
        timer_label.configure(text=time_count)


        #Minus 1 Every Second
        s -= 1

        #Seconds To Minutes
        if s > 59:
            s=0
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
            timer=False
            BackGround = PhotoImage(file = BackImages[9])
            BackGround = BackGround.subsample(3)
            CavnasImage = Label(root, image = BackGround)
            CavnasImage.place(x = 0, y = 0)


    def TimerOn():             #Turns The Timmer On
        global timer
        timer = True


    def TimerOff():            #Turns The Timer Off
        global timer
        timer = False






root=Tk()
root.title("Math Game")

canvas = Canvas(root,width=800,height=800)

Math_Game.Main_Menu()

