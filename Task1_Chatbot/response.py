from data import (greeting_responses,
    how_are_you_responses,
    jokes,
    motivational_quotes,
    )
import random
from datetime import datetime

def intro():
    print("=" * 50)
    print("🤖 Welcome to CodBot!")
    print("Type 'help' to see available commands.")
    print("Type 'bye' to exit.")
    print("=" * 50)
    

def greet():
    print ("Bot: ",(random.choice(greeting_responses)))

def how_r_u_reply():
    print( "Bot: ",(random.choice(how_are_you_responses)))

def tell_jokes():
    print("Bot: ",(random.choice(jokes)))

def motivate():
    print("Bot: ",(random.choice(motivational_quotes)))

def tell_time():
    current_time=datetime.now()
    print("Bot: ",current_time.strftime("%I:%M:%S %p"))

def tell_date():
    current_date=datetime.now()
    print("Bot: ",current_date.strftime("%d-%m-%Y"))

def exit_chat():
    print("Bot: Goodbye! Have a wonderful day. 👋")
    
def show_help():
    print("===== Available Commands =====")
    print("hello")
    print("how are you")
    print("what is your name")
    print("joke")
    print("motivate me")
    print("time")
    print("date")
    print("calculate")
    print("help")
    print("bye")

