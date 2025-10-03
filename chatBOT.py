import random
from datetime import datetime
def print_help():
    print("\n--- Command List ---")
    print("hi / hello        -> simple greeting")
    print("your name         -> find out who I am")
    print("how are you       -> casual chit-chat")
    print("time              -> current system time")
    print("date              -> today's date")
    print("joke              -> hear something silly")
    print("help              -> show this menu again")
    print("bye / exit        -> quit\n")
def run_chatbot():
    print("Chatbot : Hey there! Type 'help' if you wanna know what I can do.")
    while True:
        msg = input("You: ").strip().lower()
        if msg in ("hello", "hi"):
            print("Chatbot : Hey! Nice to see you.")
        elif "your name" in msg:
            print("Chatbot : Honestly, I don't really have a cool name yet.")
        elif "how are you" in msg:
            print("Chatbot : I'm good! Thanks for asking. How about yourself?")
        elif msg == "time":
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"Chatbot : It's {current_time} right now.")
        elif msg == "date":
            today = datetime.today().strftime("%Y-%m-%d")
            print(f"Chatbot : Today’s date is {today}.")
        elif "joke" in msg:
            silly_jokes = [
                "Why don’t scientists trust atoms? ...Because they make up everything",
                "What do you call fake spaghetti? An impasta!",
                "Why did the math book look so sad? Too many problems..."
            ]
            joke_pick = random.choice(silly_jokes)
            print("Chatbot :", joke_pick)
        elif msg in ("help", "commands"):
            print_help()
        elif msg in ("bye", "exit"):
            print("Chatbot : Okay, talk to you later!")
            break
        else:
            print("Chatbot : Hmm, not sure what that means. Try 'help'.")
if __name__ == "__main__":
    run_chatbot()