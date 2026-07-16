import random
from response import *
from data import *
from calc import *
# -------------------------------
# Welcome Message
# -------------------------------

intro()


# -------------------------------
# Main Chat Loop
# -------------------------------

while True:

    user = input("\nYou: ").strip().lower()

    if user in greetings:
        greet()

    elif user in how_are_you:
        how_r_u_reply()

    elif user in name_questions:
        print("Bot: My name is CodBot. I'm a rule-based AI chatbot built using Python.")

    elif user in thanks:
        print("Bot: You're welcome! 😊")

    elif user in jokes_commands:
        tell_jokes()

    elif user in motivation_commands:
        motivate()

    elif user in date_commands:
        tell_date()
    
    elif user in time_commands:
        tell_time()

    elif user in calci:
        expression=input("You: ")
        print("Enter your expression:")
        calculate(expression)

    elif user in help_commands:
        show_help()

    elif user in farewells:
        exit_chat()
        break

    else:
        print("Bot: Sorry, I don't understand that. Type 'help' to see available commands.")