from random import random


def random_value(min=0, max=0):
    return random() * (max - min) + min
