print(f"Lets play a game called 'Ges my number")
print('In this game the computer geuesses the number and have to find it, thenyou will gesss and the computer finds it')



import random

def randomit():
    x = random.randint(1,10)
    number = True
    global a
    a =0
    while number:
        print('I will guess a number and you will try to find it!')
        guessed_number = int(input("Please enter your guess: "))
        a += 1
        if guessed_number == x:
            
            print(f"Congratulations, you found my number in {a} efforts ")
            number = False
            
        elif guessed_number > x:
            print('The number you entered is bigger than guessed number')
        else:
            print('The number you entered is smaller than guessed number')
def myNumber():
    print('Now it is your turn to guess a number and I will find it')
    randomly = random.randint(1,11)
    print(f"The number you guessed is {randomly}. If I found press 'T', if the number you guessed is bigger then my number press'+', if it is smaller press '-")
    global b
    b = 0
    while  True:
        
        answer = input('Enter you answer here:')
        b += 1
        if answer == 'T':
            print(f"I found it in {b} efforts, thank you")
            break
        elif answer == '+':
            randomly = random.randint(randomly, 11)
            print(f"The number you guessed is {randomly}. If I found press 'T', if the number you guessed is bigger then my number press'+', if it is smaller press '-")

            
        elif answer == '-':
            randomly = random.randint(1, randomly)
            print(f"The number you guessed is {randomly}. If I found press 'T', if the number you guessed is bigger then my number press'+', if it is smaller press '-")
        else:
            print('Invalid answer choose one of them : "T", "+", "-" ')
def result():
    if a> b:
        print(f"I win with {b} efforts with {b-a} difference")
    elif b > a:
        print(f"You win with {a} efforts with {a-b} difference")
    else:
        print(f"We are durrang with {a} and {b} results")
def play():
    randomit()
    myNumber()
    result()
play()


