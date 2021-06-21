import random



operator_list = []
question_list = []
answer_List = []

operator_list.append("+")
operator_list.append("-")
operator_list.append("*")
operator_list.append("/")


operator = operator_list[random.randint(0,3)]



class Game_Questions:


    def Questions():
        global question_list, first_number, second_number, first_number_store, second_number_store


        first_number = random.randint(0,50)
        second_number = random.randint(0,50)

        first_number_store = first_number
        second_number_store = second_number

        if first_number < second_number:
            first_number = second_number_store
            second_number = first_number_store


        Game_Questions.Answers()


    def Answers():
        global question, asnwer, first_number, second_number, first_number_store, second_number_store

        question = first_number, operator, second_number
        print(question)

        



        if operator == "+":
            answer = first_number + second_number

        elif operator == "-":
            answer = first_number - second_number

        elif operator == "*":
            first_number = random.randint(0,10)
            second_number = random.randint(0,10)

            first_number_store = first_number
            second_number_store = second_number

            question = first_number, operator, second_number
            answer = first_number * second_number
        
        elif operator == "/":
            first_number = random.randint(0,10)
            second_number = random.randint(0,10)

            first_number_store = first_number
            second_number_store = second_number

            question = first_number, operator, second_number
            answer = first_number / second_number


        
            

        
            

        Game_Questions.AnswerDisplay()

    def AnswerDisplay():
        global question, asnwer

        

        





Game_Questions.Questions()