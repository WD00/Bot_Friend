import getpass
import time

your_user_name = getpass.getuser()

class Bot:
    def __init__(self, name, age, hobbies):
        self.name = name
        self.age = age
        self.hobbies = hobbies

bot1 = Bot('Botty The Bot', 'a couple of seconds', 'being your friend and being your friend.')
bot2 = Bot('DEFINITELY NOT A BOT', '37 HUMAN YEARS OLD', 'HUMAN ACTIVITIES LIKE SWIMMING.')
bot3 = Bot('rEa lLy     sAd that ..you do  N O T  lis ten to ME '+ your_user_name, '<data deleted>', 'not important. Your behaviour however, is.')

user_choice = input("Welcome to the bot center. Please pick 1 or 2.\n")

if user_choice == '1':
    user_bot = bot1
elif user_choice == '2':
    user_bot = bot2
else:
    user_bot = bot3

print('Hello! I am', user_bot.name, '. I am', user_bot.age, 'years old. My hobbies are', user_bot.hobbies, '\n')

if user_bot == bot1 or user_bot == bot2:
    user_name = input("What is your name?\n")
    print(user_name, '...Seems interesting :)')
    time.sleep(2)
    print("I thought your name was",your_user_name,"?")
elif user_bot == bot3:
    print("I'm done talking with you.")
    exit()

