from questions import QUESTIONS


def isAnswerCorrect(question, answer):

    '''
    :param question: question (Type JSON)
    :param answer:   user's choice for the answer (Type INT)
    :return:
        True if the answer is correct
        False if the answer is incorrect
    '''

    return True if answer == question["answer"] else False      #remove this


def lifeLine(ques):

    '''
    :param ques: The question for which the lifeline is asked for. (Type JSON)
    :return: delete the key for two incorrect options and return the new ques value. (Type JSON)
    '''
    a=ques["answer"]
    ab="option"+str(a)
    
    print(f'\tQuestion : {ques["name"]}' )
    print(f'\t\tOptions:')
    print(f'\t\t\tOption 1: {ques[ab]}')
    if ques[ab]!=ques["option1"]:
        print(f'\t\t\tOption 2: {ques["option1"]}')
    else:
        print(f'\t\t\tOption 2: {ques["option2"]}')
    ans = input('Your choice ( 1-2 ) : ')
    while ans not in ["1","2","quit"]:
        print("Enter a valid input")
        ans = input('Your choice ( 1-2 ) : ')
    
    if ans == "1":
        return str(a)
   
    return str(1)

def kbc():
    '''
        Rules to play KBC:
        * The user will have 15 rounds
        * In each round, user will get a question
        * For each question, there are 4 choices out of which ONLY one is correct.
        * Prompt the user for input of Correct Option number and give feedback about right or wrong.
        * Each correct answer get the user money corresponding to the question and displays the next question.
        * If the user is:
            1. below questions number 5, then the minimum amount rewarded is Rs. 0 (zero)
            2. As he correctly answers question number 5, the minimum reward becomes Rs. 10,000 (First level)
            3. As he correctly answers question number 11, the minimum reward becomes Rs. 3,20,000 (Second Level)
        * If the answer is wrong, then the user will return with the minimum reward.
        * If the user inputs "lifeline" (case insensitive) as input, then hide two incorrect options and
            prompt again for the input of answer.
        * NOTE:
            50-50 lifeline can be used ONLY ONCE.
            There is no option of lifeline for the last question( ques no. 15 ), even if the user has not used it before.
        * If the user inputs "quit" (case insensitive) as input, then user returns with the amount he has won until now,
            instead of the minimum amount.
    '''

    #  Display a welcome message only once to the user at the start of the game.
    #  For each question, display the prize won until now and available life line.
    # For now, the below code works for only one question without LIFE-LINE and QUIT checks
    print("******WELCOME TO KAUN BANEGA CROREPATI******")

    m = []
    min = 0
    a=0
    valid_input=["1","2","3","4","lifeline","quit"]

    for i in range(len(QUESTIONS)):
        print(f'\tQuestion {i}: {QUESTIONS[i]["name"]}' )
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: {QUESTIONS[i]["option1"]}')
        print(f'\t\t\tOption 2: {QUESTIONS[i]["option2"]}')
        print(f'\t\t\tOption 3: {QUESTIONS[i]["option3"]}')
        print(f'\t\t\tOption 4: {QUESTIONS[i]["option4"]}')

        ans = input('Your choice ( 1-4 ) : ')
        ans = ans.lower()


        if ans not in valid_input:
            if ans=="lifeline":
                print("Oops!!!Your LifeLine is over.")
                print("Enter some other input")
                ans = input('Your choice ( 1-4 ) : ')
                ans = ans.lower()
            while ans not in valid_input:
                print("Enter a valid input")
                ans = input('Your choice ( 1-2 ) : ')
                ans = ans.lower()

        
        if ans in valid_input:
            if ans=="lifeline":
                if i==14:
                    print("Lifeline can't be used in the last question.")
                    ans = input('Your choice ( 1-4 ) : ')
                    ans = ans.lower()
                else:
                    ans=lifeLine(QUESTIONS[i]) 
                    valid_input.remove("lifeline")
                    
            if ans=="quit":
                print("You have quit the game")
                break  
            
        # check for the input validations
             
            if isAnswerCorrect(QUESTIONS[i], int(ans) ):
            # print the total money won.
            # See if the user has crossed a level, print that if yes
                
                m.append(QUESTIONS[i]["money"])
                a=sum(m)
                print('\nCorrect !\n')
                print(f'Prize money won uptil now = {int(a)} ')
                print("If you want to quit the game,type quit")
                
                if QUESTIONS[i]["money"]==10000:
                    print("Level 1 cleared")
                    min=10000
                if QUESTIONS[i]["money"]==320000:
                    print("Level 2 cleared")
                    min=320000

            else:
            # end the game now.
            # also print the correct answer
                print('\nIncorrect !')
                #print(f'Correct answer option no {QUESTIONS[i]["answer"]}: {QUESTIONS[i]["option"+str(QUESTIONS[i]
                # ["answer"])]} ')
                print(f'Correct answer: {QUESTIONS[i]["option"+str(QUESTIONS[i]["answer"])]} ')
                if min == 0:
                    print("Minimum reward won = Rs 0")
                elif min == 10000:
                    print("Minimum reward won = Rs 10000")
                elif min == 320000:
                    print("Minimum reward won = Rs 320000")
                break
            
    if int(a)>0:
        print(f'Congrats,You have won money = Rs {int(a)} ')
            
    # print the total money won in the end.
    if sum(m)==20031000:
        print("******Congratulations, You won the game******") 


kbc()
