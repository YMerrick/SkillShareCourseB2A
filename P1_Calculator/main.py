import re

print('Our magical calculator')
print('Type quit to exit\n')

previous = 0
run = True

def performMath():
    global run

    equation = input("Enter equation: ")
    if equation == "quit":
        run = False
    else:
        previous = eval(equation)
        print ("You typed", previous)

while run:
  performMath()
