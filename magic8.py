# Name: Ciara Motter
#   Prog Purpose: This Magic 8-Ball code uses a Python tuple since the
#   user does not have the ability to change the 8-ball awnsers.
#   However, the program could have used a python list instead of a tuple.
#   NOTE: Tuples use parenthese; lists use square braces.

import random
answers_8_ball = ( "Yeah, sure, I mean it kinda makes sense", "Maybe, ask me later", "I better keep quiet for now...", "Hell no", "What the fuck",
        "That's insane lol", "What the hell? What type of question is that?", "You make no sense, try again later", "Hmmmm... Mayhaps", "Ok",
        "Are you ok", "yeah.", "From what I know, prolly not", "Nuh-uh!", "Yuh-huh!", "Yesss queeen!",
        "Please go to a psych ward.", "Wait what?", "Ok, I guess.", "I am not your therapist.",
        "Yeah totally!!", "For real for real", "Your outlook is good my G...", "Your outlook sucks lol",
        "Let me get my glasses...", "Signs point to pizza.", "Ask mom", "Someone's behind you.", )

def main():

    print("I am the most braindead Magic-8 ball, run as fast as you can. But I can answer your YES or NO questions ;)")

    another_question = True
    while another_question:
        answer = random.choice(answers_8_ball )

        print("\nShake me please :)")
        print("...Me thinks...")
        question = input("\nWhat is your YES or NO question?")
        print("Me says:" + answer)

        askAgain = input("\nWould you like to ask me another question? Please..? (Y or N)?: ")
        if askAgain.upper() == "N" or askAgain == "n":
            another_question = False

    print("\nCome back again if you need horrible life advice!")
    print("Bye-Bye :3")

main()
