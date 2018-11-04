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
    def __init__(self, difficulty)
        self.name = 'COM'
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
        self.qestions = []
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



class Game(object):
    def __init__(self, com = False,):
        self.players = []

        if com:
            com = ComputerPlayer(com)
            self.com = True
        else:
            self.com = False
