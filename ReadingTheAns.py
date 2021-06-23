from tkinter import *
import random


BackImages = ["G:\My Drive\Classroom\CDT301\Python Assesment\Math Learning Game\Layouts\Images\Game\PPM\Game#1.ppm",
            "G:\My Drive\Classroom\CDT301\Python Assesment\Math Learning Game\Layouts\Images\Game\PPM\Game#2.ppm", 
            "G:\My Drive\Classroom\CDT301\Python Assesment\Math Learning Game\Layouts\Images\Game\PPM\Game#3.ppm"]


RandomLevel = BackImages[random.randint(2,2)]


dict = {"canvas":0}

operator_list = []

operator_list.append("+")
operator_list.append("-")
operator_list.append("*")
operator_list.append("/")

operator = operator_list[random.randint(0,3)]

GameImage = BackImages


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

            first_number_store = first_number
            second_number_store = second_number

            if first_number < second_number:
                first_number = second_number_store
                second_number = first_number_store


            question = first_number, operator, second_number
            answer = first_number / second_number

            randomNumberOne = int(answer) - random.randint(0,int(answer))
            randomNumberTwo = int(answer) + random.randint(0,int(answer))


            if randomNumberOne == answer:
                randomNumberOne = int(answer) - random.randint(0,int(answer))
            
            if randomNumberTwo == answer:
                randomNumberTwo = int(answer) + random.randint(0,int(answer))



        Game_Questions.AnswerDisplay()


    #--------------------------------------MAKE THE OPERATOR CHANGE WHEN A NEW QUESITON IS MADE-------------------------------------------#


    def AnswerDisplay():
        global question, answer, randomNumberOne, randomNumberTwo

        dict["canvas"] = canvas
        canvas.delete('all')

        answerList = []

        answerList.append(int(answer))
        answerList.append(int(randomNumberOne))
        answerList.append(int(randomNumberTwo))

        print(question)


        #Importing the image onto the canvas
        BackGround = PhotoImage(file = RandomLevel)
        BackGround = BackGround.subsample(3)
        CavnasImage = Label(root, image = BackGround)
        CavnasImage.place(x = 0, y = 0)


        if RandomLevel == BackImages[0]:
            #Creates the buttons
            answerOne = Button(root,text=answerList[random.randint(0,2)],font="Times 18 bold",width = 7, height = 1, bg = 'red', highlightthickness = 0, bd = 0, command=print("AnswerOne"))
            answerTwo = Button(root,text=answerList[random.randint(0,2)],font="Times 18 bold",width = 7, height = 1, bg = 'red', highlightthickness = 0, bd = 0, command=print("AnswerTwo"))
            answerThree = Button(root,text=answerList[random.randint(0,2)],font="Times 18 bold",width = 7, height = 1, bg = 'red', highlightthickness = 0, bd = 0, command=print("AnswerThree"))

            #Displays the buttons
            answerOne_canvas = canvas.create_window( 0, 0, anchor = "nw",window = answerOne)
            answerTwo_canvas = canvas.create_window( 100, 100, anchor = "nw",window = answerTwo)
            answerThree_canvas = canvas.create_window( 200, 200, anchor = "nw",window = answerThree)

            #Makes the Question Label
            question_label = Label(root, text = question, font="Times 35 bold",width = 7, height = 1, bg = 'purple')
            question_label.place(x=325,y=720)
    
        elif RandomLevel == BackImages[1]:
            #Creates the buttons
            answerOne = Button(root,text=answerList[random.randint(0,2)],font="Times 18 bold",width = 7, height = 1, bg = 'red', highlightthickness = 0, bd = 0, command=print("AnswerOne"))
            answerTwo = Button(root,text=answerList[random.randint(0,2)],font="Times 18 bold",width = 7, height = 1, bg = 'red', highlightthickness = 0, bd = 0, command=print("AnswerTwo"))
            answerThree = Button(root,text=answerList[random.randint(0,2)],font="Times 18 bold",width = 7, height = 1, bg = 'red', highlightthickness = 0, bd = 0, command=print("AnswerThree"))

            #Displays the buttons
            answerOne_canvas = canvas.create_window( 0, 0, anchor = "nw",window = answerOne)
            answerTwo_canvas = canvas.create_window( 100, 100, anchor = "nw",window = answerTwo)
            answerThree_canvas = canvas.create_window( 200, 200, anchor = "nw",window = answerThree)

            #Makes the Question Label
            question_label = Label(root, text = question, font="Times 35 bold",width = 7, height = 1, bg = 'purple')
            question_label.place(x=325,y=720)
    
        elif RandomLevel == BackImages[2]:
            #Makes Buttons
            answerOne = Button(root,text=answerList[random.randint(0,2)],font="Times 18 bold",width = 7, height = 1, bg = 'red', highlightthickness = 0, bd = 0, command=print(" "))
            answerTwo = Button(root,text=answerList[random.randint(0,2)],font="Times 18 bold",width = 7, height = 1, bg = 'red', highlightthickness = 0, bd = 0, command=print(" "))

            #Displays the buttons
            answerOne_canvas = canvas.create_window( 125, 50, anchor = "nw",window = answerOne)
            answerTwo_canvas = canvas.create_window( 680, 200, anchor = "nw",window = answerTwo)

            #Makes the Question Label
            question_label = Label(root, text = question, font="Times 35 bold",width = 7, height = 1, bg = 'purple')
            question_label.place(x=325,y=720)




            #Testing Button
            testingButton = Button(root, text="TESING BUTTON!!!!", font = "Times 15 bold",width=20, height=1,bg='yellow', command=Game_Questions.Questions)
            testingButton_Canvas = canvas.create_window(100,600, anchor = "nw", window = testingButton)
    



        dict["canvas"].pack()
        root.mainloop()



        
root=Tk()
root.title("Math Game")

canvas = Canvas(root,width=800,height=800)
        
Game_Questions.Questions()