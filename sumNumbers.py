#!/usr/local/bin/python

class Maths(object):
    def __init__(self):
        pass

    def sum(self, number1, number2):
        return number1 + number2


if __name__ == "__main__":
    py = Maths()
    ret = py.sum(10 , 20)
    print ret
