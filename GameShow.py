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

class Questions(object):
    def __init__(self):
        self.qestions = []
        self.answers = []

    def askQuestion(self):
        idx = random.randint(0,len(questions))
        question = questions[idx]
        answer = answer[idx]
        del question[idx]
        del answer[idx]
        return question, answer



class Game(object):
    def __init__(self):
        self.

    def
