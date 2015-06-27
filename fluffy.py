
import colors as c
from ultils import ask
import random


"Welcome to the Pink Fluffy Unicorns quiz. Lets test your knowledge..:."


def correct():
    print(c.green + "correct")

def incorrect():
    print(c.red + "incorrect")

def q1():
    answer = ask("What color is the Uincorns fur")
    if answer == "pink":
        return True
    return False

def q2():
    answer = ask("What are the Unicorns dancing on")
    if answer == "rainbows":
        return True           
    return False

def q3():
    answer = ask("What word discribes the Unicorns fur")
    if answer == "smiles":
        return True
    return False
     


questions = [q1, q2, q3]








