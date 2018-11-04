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
    def __init__(self, name, difficulty)
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

    def askQuestion(self):
        idx = random.randint(0,len(questions))
        question = questions[idx]
        answer = answers[idx]
        choices = answerChoices[idx]
        del question[idx]
        del answer[idx]
        del answerChoices[idx]
        return question, answer


def turn():





def main():
    print("Welcome to our trivia game")
    print("We have a few questions before we begin")
    comp = input("How many computers do you want to play against? (int)")

    if comp >= 0:
        dif = input("How smart do you want the computers to be?")

    numofPlayer = input("How many human players will there to be? (int)")

    Players = []
    for i in range(numofPlayer):
        name = input('Player ',str(i),"Name:")
        Players.append(Player(name))
    
    for i in range(comp):
        name = "comp" + str(i)
        Players.append(ComputerPlayer(name,dif))

    # Read in Questions and Answers
    file = open('QA.txt','r')


    turn(Players)



main()
