# GameShow
import random, tkinter, tkinter.ttk

# classes
class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0

    def getScore(self):
        return (self.score)

    def updateScore(self, points):
        self.score += points

    def __str__(self):
        return '{}\'s score is {}'.format(self.name, self.score)


class ComputerPlayer:

    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty
        self.score = 0

    def getScore(self):
        return (self.score)

    def updateScore(self, points):
        self.score += points

    def response(self, idx, question, answer, answers):
        # easy setting returns random answer
        if (self.difficulty.upper() == 'EASY'):
            idx = random.randint(0,len(answers)-1)
            ans = answers[idx].split(".")
            ans = ans[0]
            return ans
        # medium setting returns random answer if correct, or tries again and
        # returns that answer
        elif(self.difficulty.upper() == 'MEDIUM'):
            idx = random.randint(0,len(answers)-1)
            if answerChoices[idx] == answer:
                ans = answers[idx].split(".")
                ans = ans[0]
                return answers[idx]
            else:
                idx = random.randint(0,len(answers)-1)
                ans = answers[idx].split(".")
                ans = ans[0]
                return answers[idx]
        # hard setting returns correct answer
        else:
            return answer


class Questions:
    def __init__(self):
        self.questions = []
        self.answers = []
        self.answerChoices = []

    def numofQuestions(self):
        return(len(self.questions))

    def askQuestion(self):

        idx = random.randint(0,len(self.questions)-1)
        question = self.questions[idx]
        answer = self.answers[idx]
        choices = self.answerChoices[idx]

        return question, answer, choices, idx

    def delQuestion(self, question, answer, choices,idx):
        del self.questions[idx]
        del self.answers[idx]
        del self.answerChoices[idx]


def scoreboard(players, coms):
    print("The Scoreboard:")
    for player in players:
        print(player.name +"---->" +str(player.getScore()))
    for com in coms:
        print(com.name +"---->" +str(com.getScore()))


def turn(players,coms,questions, terminateCondition):
    stop = 0
    while questions.numofQuestions() > 0:
        for player in players:

            question, Correctanswer, answerChoices, idx = questions.askQuestion()
            print(player.name + "'s Turn: \n")
            print(question + "\n")
            for i in range(0, len(answerChoices)):
                print(answerChoices[i])
            playerAnswer = input("\nWhat is your answer? \n")
            playerAnswer = playerAnswer.upper()

            if playerAnswer == "SCOREBOARD":
                print('\n')
                scoreboard(players, coms)
                print('\n')
                print(question + '\n')
                for i in range(0, len(answerChoices)):
                    print(answerChoices[i])
                playerAnswer = input("\nWhat is your answer? \n")
                playerAnswer = playerAnswer.upper()
            if (playerAnswer == "STOP"):
                stop = 1
                break

            if playerAnswer == Correctanswer:
                print("\nYou are correct \n")
                player.updateScore(1)
                questions.delQuestion(question,Correctanswer,answerChoices,idx)
            else:
                print("\nYou are incorrect \n")
                #let all the other players guess the incorrect question to steal points

                questions.delQuestion(question,Correctanswer,answerChoices,idx)

            if questions.numofQuestions()>0:
                input('Continue to Next Question? (Enter)\n\n')
            if int(terminateCondition) == player.getScore() and int(terminateCondition) != 0:
                print(player.name +" reached a score of "+ str(player.getScore()))
                print(player.name + " Wins!!")
                return
        if (stop == 1):
        	break

        #com will simulation
        for com in coms:
            question, Correctanswer, answerChoices, idx = questions.askQuestion()
            print(com.name + "'s Turn: \n")
            print(question + "\n")
            for i in range(0, len(answerChoices)):
                print(answerChoices[i])
            #adjust response for com
            comAnswer = com.response(idx, question, Correctanswer, answerChoices)
            print("\n" + com.name + "'s answer: " + comAnswer)
            comAnswer =  comAnswer.upper()

            if comAnswer == Correctanswer:
                print("\nYou are correct \n")
                com.updateScore(1)
                questions.delQuestion(question,Correctanswer,answerChoices,idx)
            else:
                print("\nYou are incorrect \n")
                # let all the other players guess the incorrect question to steal points

                questions.delQuestion(question,Correctanswer,answerChoices,idx)
            if int(terminateCondition) == com.getScore() and int(terminateCondition) != 0:
                print(com.name +"reached a score of "+ str(com.getScore()))
                print(com.name + "Wins!!")
                return

    print("\n\nGAME OVER\n\n")
    scoreboard(players, coms)
    print('\n')

    winner = ''
    second = ''
    nextBest = 0
    maxScore = 0

    for player in players:

        if player.getScore() >= maxScore:
            nextBest = maxScore
            second = player.name
            maxScore = player.getScore()

            second = winner
            winner = player.name

    for com in coms:
        if com.getScore() >= maxScore:
            nextBest = maxScore
            second = com.name
            maxScore = com.getScore()

            second = winner
            winner = com.name

    if maxScore == 0:
        print("No winner :(")
    elif nextBest == maxScore:
        print("It's a tie between " + str(second) + " and", str(winner) + "!")
    else:
        print(winner + " Wins!!!")

# Game setup
def main():

    # when button is clicked, the entry in text will replace label
    def onClickCombo():
        label.configure(text="input: " + combo.get())
    '''
    # Labels and input widgets
    label = tkinter.Label(window, text="Hello", font=("Times New Roman", 50))
    label.grid(column=1, row=2)

    text = tkinter.Entry(window, width=10)
    text.grid(column=1, row=4)

    combo = tkinter.ttk.Combobox(window)
    combo['values']= ("Select", 1, 2, 3, 4, 5)
    combo.current(0)
    combo.grid(column=3, row=4)

    # Buttons
    textButton = tkinter.Button(window, text="Submit", bg="grey", fg="black", command=onClickText)
    textButton.grid(column=1, row=6)

    comboButton = tkinter.Button(window, text="Submit", bg="grey", fg="black", command=onClickCombo)
    comboButton.grid(column=3, row=6)
    '''
    # Putting the code for different widgets here for now
    window = tkinter.Tk()
    window.geometry("550x700")
    window.title("Let's Play Sports Trivia!")

    # Switch frames
    def raiseFrame(frame):
        frame.tkraise()

    # when quitButton is clicked, the GUI window will close and the application will be aborted
    def closeWindow(wndw):
        wndw.destroy()
        exit() # comment this out to use command line

    def onClickSubmit():
        global comp
        global dif
        global numofPlayer
        global diffLevel
        global terminateCondition

        comp = int(spin1.get())
        dif = combo1.get().lower()
        numofPlayer = int(spin2.get())
        diffLevel = combo2.get().lower()
        terminateCondition = int(spin3.get())

        window.destroy()

    label1 = tkinter.Label(window, text="\tWelcome to our trivia game!\n\tWe have a few questions before we begin:\n\n", font=("Times New Roman", 20))
    label1.grid(column=1, row=2)

    label2 = tkinter.Label(window, text="How many computers do you want to play against?\n", font=("Times New Roman", 20))
    label2.grid(column=1, row=4)
    spin1 = tkinter.Spinbox(window, from_=0, to=5, width=10)
    spin1.grid(column=1,row=5)

    label3 = tkinter.Label(window, text="\nHow smart should the computers be?\n", font=("Times New Roman", 20))
    label3.grid(column=1, row=7)
    combo1 = tkinter.ttk.Combobox(window)
    combo1['values']= ("No Computer", "Easy", "Medium", "Hard")
    combo1.current(0)
    combo1.grid(column=1, row=8)

    label4 = tkinter.Label(window, text="\nHow many human players will there be?\n", font=("Times New Roman", 20))
    label4.grid(column=1, row=10)
    spin2 = tkinter.Spinbox(window, from_=1, to=3, width=10)
    spin2.grid(column=1,row=11)

    label5 = tkinter.Label(window, text="\nHow hard should the questions be?\n", font=("Times New Roman", 20))
    label5.grid(column=1, row=13)
    combo2 = tkinter.ttk.Combobox(window)
    combo2['values']= ("Easy", "Medium", "Hard")
    combo2.current(0)
    combo2.grid(column=1, row=14)

    label6 = tkinter.Label(window, text="\nChoose win condition a number of points or infinite?\n(0 for infinite) \n", font=("Times New Roman", 20))
    label6.grid(column=1, row=15)
    spin3 = tkinter.Spinbox(window, from_=0, to=1000000, width=10)
    spin3.grid(column=1,row=16)

    quitButton = tkinter.Button(window, text="Quit", bg="white", fg="red", command=lambda:closeWindow(window))
    quitButton.grid(column=12, row=0)

    submitButton = tkinter.Button(window, text="Submit", bg="grey", fg="black", command=onClickSubmit)
    submitButton.grid(column=1, row=18)

    window.mainloop()
    '''
    comp = input("How many computers do you want to play against?\n")
    while True:
        try:
            comp = int(comp)
            break
        except:
            print("\nInvalid Input: must be a number\n")
            comp = input()

    if comp > 0:
        dif = input("\nSelect the computer difficulty. (easy/medium/hard) \n")
        while dif.lower() not in ["easy", "medium", "hard"]:
            print("\nSelect easy, medium, or hard")
            dif = input()
        dif = dif.lower()

    numofPlayer = input("\nHow many human players will there be? (Up to 3 players) \n")
    while True:
        try:
            numofPlayer = int(numofPlayer)
            if numofPlayer in [1, 2, 3]:
                break
            else:
                print("\nInvalid Input: 1 to 3 players required\n")
                numofPlayer = input()
        except:
            print("\nInvalid Input: 1 to 3 players required\n")
            numofPlayer = input()

    diffLevel = input("\nType question difficulty level (easy/medium/hard) \n")
    while diffLevel.lower() not in ["easy", "medium", "hard"]:
        print("\nSelect easy, medium, or hard")
        diffLevel = input()
    diffLevel = diffLevel.lower()

    while diffLevel not in ["easy", "medium", "hard"]:
        print("\nSelect easy, medium, or hard")
        diffLevel = input()
        diffLevel = diffLevel.lower()
    '''

    nameWindow = tkinter.Tk()
    nameWindow.geometry("900x650")
    nameWindow.title("Let's See Who is Playing")

    # when button is clicked, the entry in text will replace label
    def onClickText():
        global name
        name = str(text.get())
        nameWindow.destroy()

    labelTxt = "Enter Player the " + str(numofPlayer) + "'s names (Ex: user1, user2, user3):"
    label7 = tkinter.Label(nameWindow, text=str(labelTxt), font=("Times New Roman", 20))
    label7.grid(column=1, row=0)
    text = tkinter.Entry(nameWindow, width=10)
    text.grid(column=1, row=2)
    textButton = tkinter.Button(nameWindow, text="Submit", bg="grey", fg="black", command=onClickText)
    textButton.grid(column=1, row=4)
    quitButton = tkinter.Button(nameWindow, text="Quit", bg="white", fg="red", command=lambda:closeWindow(nameWindow))
    quitButton.grid(column=12, row=0)
    nameWindow.mainloop()

    global name
    names = name.split(', ')

    Players = []
    for i in range(0, len(names)):
        #name = input('\nPlayer ' + str(i) + " Name: ")
        Players.append(Player(str(names[i])))

    Coms = []
    for i in range(1, comp+1):
        name = "comp" + str(i)
        Coms.append(ComputerPlayer(name,dif))

    for i in Players:
        print (str(i))
    # Read in Questions and Answers
    file = str(diffLevel + "QA" + ".txt")
    lines = [line.rstrip('\n') for line in open(file)]
    lines = [line.lstrip('\t') for line in lines]

    for line in lines:
        if len(line) == 0:
            lines.remove(line)
    lines.remove(lines[-1])

    QA = Questions()

    for line in lines:

        # Multiple Choice
        if line[0] == '!':
            index = line.find('"')
            QA.questions.append(line[index + 1: -1])
            mc = []
            ans = ''

            index = lines.index(line)
            i=1
            while i <= 4:
                mc.append(lines[index + i])
                i+=1

            ans = lines[index + 5]
            ans = ans[1:]

            QA.answers.append(ans)
            QA.answerChoices.append(mc)


        # True False
        if line[0] == '$':
            index = line.find('"')
            QA.questions.append(line[index + 1: -1])

            TF = []
            ans = ''

            index = lines.index(line)

            i=1
            while i <= 2:
                TF.append(lines[index + i])
                i += 1

            ans = lines[index + 3]
            ans = ans[1:]

            QA.answers.append(ans)
            QA.answerChoices.append(TF)

    #print(QA.questions)

    #print(QA.answerChoices)

    #print(QA.answers)
    input("\nPress Enter to continue to game")
    print("\nBegin Game!!\n")
    turn(Players, Coms, QA, terminateCondition)

    playAgain = input("\nPlay Again? (y/n)\n")
    playAgain.lower()
    if playAgain == 'y' or playAgain == 'yes':
        main()
    else:
        exit()

main()
