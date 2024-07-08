while True:

     print("       🕸🦴    TREASURE GAME      👀💰")
     print("welcome to my island".capitalize())
     print(" there are a two doors in front of you, a red door 🚪 and a blue door 🚪".capitalize())
     choose = input("which door do you want to open a red door 🚪 or a blue door 🚪?").capitalize().strip()
     if choose == "Blue":
       print("oops! there is an corcodile 🐊\n game over!".capitalize())
     elif choose== "Red":
        print("Great! you entered a correct room \n you found three boxes 📦🎁📦:white box, black box, green box".capitalize())
        box = input("choose a box 📦 to open it between (white box📦, black box📦, green box📦".capitalize().strip())
        if box == "White":
             print("oops you entered a box📦 filled with snake 🐍 \n game over ".capitalize())
        elif box == "black":
             print("oops! you entered a box📦 filled with spiders 🕸🕷 \n Game over".capitalize())
        elif box == "green":
            print("congratulations! you found the corect box🎁 and the treaure and you got 💵$1,000,000$💰".capitalize())
        else:
             print("invalid answer".capitalize()) 
     else: 
       print("invalid answer".capitalize()) 
     game =  input("do you want to play again (yes or no)".strip().capitalize())
     if game == "no":
         break
     