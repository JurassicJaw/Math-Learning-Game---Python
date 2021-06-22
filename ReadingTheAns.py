from tkinter import *
import random


BackImages = ["G:\My Drive\Classroom\CDT301\Python Assesment\Math Learning Game\Layouts\Images\Game\PPM\Game#1.ppm",
            "G:\My Drive\Classroom\CDT301\Python Assesment\Math Learning Game\Layouts\Images\Game\PPM\Game#2.ppm",
            "G:\My Drive\Classroom\CDT301\Python Assesment\Math Learning Game\Layouts\Images\Game\PPM\Game#3.ppm"]



dict = {"canvas":0}

operator_list = []

operator_list.append("+")
operator_list.append("-")
operator_list.append("*")
operator_list.append("/")


operator = operator_list[random.randint(0,3)]



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


        Game_Questions.Answers()

    def Answers():
        global question, answer, first_number, second_number, first_number_store, second_number_store, randomNumberOne, randomNumberOneStore, randomNumberTwo, randomNumberTwoStore

        question = first_number, operator, second_number


        if operator == "+":
            answer = first_number + second_number

            randomNumberOne = int(answer) - random.randint(0,int(answer))
            randomNumberTwo = int(answer) + random.randint(0,int(answer))

            if randomNumberOne == answer:
                randomNumberOne = int(answer) - random.randint(0,int(answer))
            
            if randomNumberTwo == answer:
                randomNumberTwo = int(answer) + random.randint(0,int(answer))


        elif operator == "-":
            answer = first_number - second_number

            if first_number < second_number:
                first_number_store = first_number
                second_number_store = second_number

            randomNumberOne = int(answer) - random.randint(0,int(answer))
            randomNumberTwo = int(answer) + random.randint(0,int(answer))

            if randomNumberOne == answer:
                randomNumberOne = int(answer) - random.randint(0,int(answer))
            
            if randomNumberTwo == answer:
                randomNumberTwo = int(answer) + random.randint(0,int(answer))


        elif operator == "*":
            first_number = random.randint(1,10)
            second_number = random.randint(1,10)

            question = first_number, operator, second_number
            answer = first_number * second_number

            randomNumberOne = int(answer) - random.randint(0,int(answer))
            randomNumberTwo = int(answer) + random.randint(0,int(answer))

            if randomNumberOne == answer:
                randomNumberOne = int(answer) - random.randint(0,int(answer))
            
            if randomNumberTwo == answer:
                randomNumberTwo = int(answer) + random.randint(0,int(answer))

            
        elif operator == "/":
            first_number = random.randint(1,10)
            second_number = random.randint(1,10)

            if first_number < second_number:
                first_number_store = second_number
                second_number_store = first_number


            question = first_number, operator, second_number
            answer = first_number / second_number

            randomNumberOne = int(answer) - random.randint(0,int(answer))
            randomNumberTwo = int(answer) + random.randint(0,int(answer))


            if randomNumberOne == answer:
                randomNumberOne = int(answer) - random.randint(0,int(answer))
            
            if randomNumberTwo == answer:
                randomNumberTwo = int(answer) + random.randint(0,int(answer))



        Game_Questions.AnswerDisplay()

    def AnswerDisplay():
        global question, answer, randomNumberOne, randomNumberTwo

        dict["canvas"] = canvas

        answerList = []

        answerList.append(int(answer))
        answerList.append(int(randomNumberOne))
        answerList.append(int(randomNumberTwo))


        #Importing the image onto the canvas
        BackGround = PhotoImage(file = BackImages[0])
        BackGround = BackGround.subsample(3)
        CavnasImage = Label(root, image = BackGround)
        CavnasImage.place(x = 0, y = 0)

        if BackImages == BackImages[0]:

            #Creates the buttons
            answerOne = Button(root,text=answerList[random.randint(0,2)],font="Times 18 bold",width = 7, height = 1, bg = 'red', highlightthickness = 0, bd = 0, command=print("TESTETSETSTTTTT"))

            #Displays the buttons
            answerOne_canvas = canvas.create_window( 75, 175, anchor = "nw",window = answerOne)
        
        elif BackImages == BackImages[1]:
            #Creates the buttons
            answerOne = Button(root,text=answerList[random.randint(0,2)],font="Times 18 bold",width = 7, height = 1, bg = 'red', highlightthickness = 0, bd = 0, command=print("TESTETSETSTTTTT"))

            #Displays the buttons
            answerOne_canvas = canvas.create_window( 75, 175, anchor = "nw",window = answerOne)
        
        elif BackImages == BackImages[2]:
            #Creates the buttons
            answerOne = Button(root,text=answerList[random.randint(0,2)],font="Times 18 bold",width = 7, height = 1, bg = 'red', highlightthickness = 0, bd = 0, command=print("TESTETSETSTTTTT"))

            #Displays the buttons
            answerOne_canvas = canvas.create_window( 75, 175, anchor = "nw",window = answerOne)



        dict["canvas"].pack()
        root.mainloop()



        
root=Tk()
root.title("Math Game")

canvas = Canvas(root,width=800,height=800)
        
Game_Questions.Questions()