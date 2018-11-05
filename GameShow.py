# GameShow
import random

class Player(object):
    def __init__(self, name):
        self.name = name
        self.score = 0

    def getScore(self):
        return (self.score)

    def updateScore(self, points):
        self.score += points

    def __str__(self):
        return '{s}\'s score is {d}'.format(self.name, self.points)

class ComputerPlayer(object):
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty
        self.score = 0

    def response(self, idx, question, answer, answers):
        # easy setting returns random answer
        if (self.difficulty.upper() == 'EASY'):
            idx = random.randint(0,len(questions))
            return answers[idx]
        # medium setting returns random answer if correct, or tries again and
        # returns that answer
        elif(self.difficulty.upper() == 'MEDIUM'):
            idx = random.randint(0,len(questions))
            if answers[idx] == answer:
                return answers[idx]
            else:
                idx = random.randint(0,len(questions))
                return answers[idx]
        # hard setting returns correct answer
        else:
            return answer


class Questions(object):
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
    
        return question, answer , choices, idx

    def delQuestion(self, question, answer, choices,idx):
        del self.questions[idx]
        del self.answers[idx]
        del self.answerChoices[idx]


def scoreboard(players):
    print("The Scoreboard:")
    for player in players:
        print(player.name +"---->" +str(player.getScore()))

def turn(players,questions):
    while questions.numofQuestions() > 0:    
        for player in players:
        
            question, Correctanswer, answerChoices, idx = questions.askQuestion()
            print(player.name + "'s Turn:")
            print(question)
            for i in range(0, len(answerChoices)):
                print(answerChoices[i])
            playerAnswer = input("What is your answer?")
            playerAnswer =  playerAnswer.upper()

            if playerAnswer == "SCOREBOARD":
                scoreboard(players)
                print(question)
                for i in range(0, len(answerChoices)):
                    print(answerChoices[i])
                playerAnswer = input("What is your answer?")
                playerAnswer =  playerAnswer.upper()

            if playerAnswer == Correctanswer:
                print("You are correct")
                player.updateScore(1)
                questions.delQuestion(question,Correctanswer,answerChoices,idx)
            else:
                print("You are incorrect")
                questions.delQuestion(question,Correctanswer,answerChoices,idx)


def main():
    print("Welcome to our trivia game \n")
    print("We have a few questions before we begin \n")
    comp = input("How many computers do you want to play against? (int)\n")

    if int(comp) > 0:
        dif = input("How smart do you want the computers to be? \n")

    numofPlayer = input("How many human players will there to be? (int) \n")

    Players = []
    for i in range(int(numofPlayer)):
        name = input('Player ' + str(i) + " Name: ")
        Players.append(Player(name))
    
    for i in range(int(comp)):
        name = "comp" + str(i)
        Players.append(ComputerPlayer(name,dif))

    # Read in Questions and Answers
    lines = [line.rstrip('\n') for line in open('QA.txt')]
    lines = [line.lstrip('\t') for line in lines]

    for line in lines:
        if len(line) == 0:
            lines.remove(line)
    lines.remove(lines[-1])

    QA = Questions()
    
    for line in lines:

        # Multipe Choice
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
                i+=1

            ans = lines[index + 3]
            ans = ans[1:]

            QA.answers.append(ans)
            QA.answerChoices.append(TF)

    #print(QA.questions)

    #print(QA.answerChoices)

    #print(QA.answers)

    turn(Players, QA)

main()