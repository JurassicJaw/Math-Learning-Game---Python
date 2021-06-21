from tkinter import *

s = 59
m = 0
h = 0
score = 0

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
                "G:\My Drive\Classroom\CDT301\Python Assesment\Math Learning Game\Layouts\Images\Buttons\PNG\Title.png"]          # Title (8)


def Timer():
    global s, m, h, timer

    if timer == True:

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
            print("TIMES UP")

        #Loop
        print(h,m,s)
        root.after(1000, Timer)

    #Sets everything to 0 when False
    elif timer == False:
        s = 0
        m = 0
        h = 0
        print("Stopped")
        print("Your score is ", score)



def CorrectAnswer():
    global s,m,h,timer,score

    s += 10
    score +=10

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
        print("TIMES UP")

    print(h,m,s)

def WrongAnswer():
    global s,m,h,timer,score

    s -= 10
    score -= 10

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
        print("TIMES UP")

    print(h,m,s)


def TimerOn():
    global timer
    timer = True

def TimerOff():
    global timer
    timer = False


def menu():
    global timer, s, m, h

    timer=False

    dict["canvas"] = canvas

    #Importing the image onto the canvas
    BackGround = PhotoImage(file = BackImages[3])
    BackGround = BackGround.subsample(3)
    CavnasImage = Label(root, image = BackGround)
    CavnasImage.place(x = 0, y = 0)

    #Buttons
    StartButton = PhotoImage(file = ButtonImages[7])
    StartButton = StartButton.subsample(3)
    Start = Button(root,text="",image=StartButton,highlightthickness=0,bd=0,command=lambda:[TimerOn(),Timer()])

    StopButton = PhotoImage(file = ButtonImages[5])
    StopButton = StopButton.subsample(3)
    Stop = Button(root,text="",image=StopButton,highlightthickness=0,bd=0,command=lambda:[TimerOff(),Timer()])

    AddTimeButton = PhotoImage(file = ButtonImages[4])
    AddTimeButton = AddTimeButton.subsample(3)
    AddTime = Button(root,text="",image=StopButton,highlightthickness=0,bd=0,command=CorrectAnswer)

    MinusButton = PhotoImage(file = ButtonImages[4])
    MinusButton = MinusButton.subsample(3)
    MinusTime = Button(root,text="",image=StopButton,highlightthickness=0,bd=0,command=WrongAnswer)


    Start_canvas = canvas.create_window( 300, 400, anchor = "nw",window = Start)
    Stop_canvas = canvas.create_window( 300, 500, anchor = "nw",window = Stop)
    AddTime_canvas = canvas.create_window( 300, 600, anchor = "nw",window = AddTime)
    MinusTime_canvas = canvas.create_window( 300, 700, anchor = "nw",window = MinusTime)



    dict["canvas"].pack()
    root.mainloop()


    

root=Tk()
canvas = Canvas(root,width=800,height=800,bg="grey25")

menu()