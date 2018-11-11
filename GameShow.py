# GameShow
import random, tkinter

'''
window = tkinter.Tk()
window.geometry("600x300")
window.title("Let's Play Sports Trivia!")

label = tkinter.Label(window, text="Hello", font=("Times New Roman", 50))
label.grid(column=1, row=2)

text = tkinter.Entry(window, width=10)
text.grid(column=1, row=4)

def clicked():
    label.configure(text="input: " + text.get())

button = tkinter.Button(window, text="Click Me", bg="grey", fg="black", command=clicked)
button.grid(column=1, row=6)

window.mainloop()
'''

class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0

    def getScore(self):
        return (self.score)

    def updateScore(self, points):
        self.score += points

    def __str__(self):
        return '{s}\'s score is {d}'.format(self.name, self.points)


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


def turn(players,coms,questions):
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

def main():
    print("\nWelcome to our trivia game! \n")
    print("We have a few questions before we begin: \n")

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


    Players = []
    for i in range(1, int(numofPlayer)+1):
        name = input('\nPlayer ' + str(i) + " Name: ")
        Players.append(Player(name))

    Coms = []
    for i in range(1, comp+1):
        name = "comp" + str(i)
        Coms.append(ComputerPlayer(name,dif))

    # Read in Questions and Answers
    lines = [line.rstrip('\n') for line in open(str(diffLevel + "QA" + ".txt"))]
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
    turn(Players, Coms, QA)


main()
