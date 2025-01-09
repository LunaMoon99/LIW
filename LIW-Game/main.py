import turtle
#------------------Functions--------------------------------
def startingPt():
  pos(-200, 0)
  bg("map.png", 700, 485)
  print("\nLuna is at the Starting Point, here are her options:")
  print("1. Go into the Rose Garden")
  print("2. Go into the Mad Hatter's Tea Party")
  print("3. Go forward")
  print("4. Check inventory")
  print("5. Check instructions")
  ans = input("What should Luna do? Choose between (1-5): ")
  if ans == ("1"):
    roseGarden()
  elif ans == ("2"):
    teaParty()
  elif ans == ("3"):
    middlePt()
  elif ans == ("4"):
    inventory()
    startingPt()
  elif ans == ("5"):
    instructions()
    startingPt()
  else:
    print("\nPlease try again")
    startingPt()

def middlePt():
  pos(0, 0)
  bg("map.png", 700, 485)
  print("\nLuna is at the Middle Point, here are her options:")
  print("1. Go into the Hearts Castle")
  print("2. Go into the Mad Hatter's Tea Party")
  print("3. Go forward")
  print("4. Go back")
  print("5. Check inventory")
  print("6. Check instructions")
  ans = input("What should Luna do? Choose between (1-6): ")
  if ans == ("1"):
    heartsCastle()
  elif ans == ("2"):
    teaParty()
  elif ans == ("3"):
    lastPt()
  elif ans == ("4"):
    startingPt()
  elif ans == ("5"):
    inventory()
    middlePt()
  elif ans == ("6"):
    instructions()
    middlePt()
  else:
    print("\nPlease try again")
    middlePt()

def lastPt():
  pos(200, 0)
  bg("map.png", 700, 485)
  print("\nLuna is at the Last Point, here are her options:")
  print("1. Go into the Mushroom Field")
  print("2. Go into the Mad Hatter's Tea Party")
  print("3. Go back")
  print("4. Check inventory")
  print("5. Check instructions")
  ans = input("What should Luna do? Choose between (1-5): ")
  if ans == ("1"):
    mushroomField()
  elif ans == ("2"):
    teaParty()
  elif ans == ("3"):
    middlePt()
  elif ans == ("4"):
    inventory()
    lastPt()
  elif ans == ("5"):
    instructions()
    lastPt()
  else:
    print("\nPlease try again")
    lastPt()

def roseGarden():
  if "rg" not in tasks:
    luna.hideturtle()
    bg("rG.png", 700, 525)
    print("\nLuna is at the Rose Garden, here are her options:")
    print("1. Talk to the Card Soldier")
    print("2. Paint the roses")
    print("3. Go back")
    print("4. Check inventory")
    print("5. Check instructions")
    ans = input("What should Luna do? Choose between (1-5): ")
    if ans == ("1"):
      print("\nAs Luna goes up to the Card Soldier, he is struggling to paint a white rose red. He sees you approaching and has a confused look on his face. Luna explains her situation and he agrees to help her out. \n'You'll want to paint the white rose with the least amount of petals first and count up from there,' he tells her as he gives her the red paint and paintbrush.")
      if "Red Paint and Paintbrush" not in luna_inventory:
        luna_inventory.append("Red Paint and Paintbrush")
        print("\nLuna has obtained a 'Red Paint and Paintbrush'")
      input("Press any key to continue")
      roseGarden()
    elif ans == ("2"):
      if "Red Paint and Paintbrush" not in luna_inventory:
        print("\nYou don't have red paint nor a paintbrush, try asking the Card Soldier for help")
        roseGarden()
      else:
        print("\nWhich one should Luna paint first?")
        num = input("Choose between 1-5: ")
        if num == "2":
          bg("rose1.png", 700, 525)
          print("You painted correctly!")
          num = input("\nChoose between 1, 3, 4, or 5: ")
        else:
          repaint()
        if num == "5":
            bg("rose2.png", 700, 525)
            print("You painted correctly!")
            num = input("\nChoose between 1, 3, or 4: ")
        else: 
          repaint()
        if num == "3":
          bg("rose3.png", 700, 525)
          print("You painted correctly!")
          num = input("\nChoose between 1 or 4: ")
        else:
          repaint()
        if num == "1":
          bg("rose4.png", 700, 525)
          print("You painted correctly!")
          input("Press any key to paint the last rose")
          bg("rose5.png", 700, 525)
          print("\nYou've completed the Rose Garden")
          input("Press any key to continue")
          tasks.append("rg")
          startingPt()
        else:
          repaint()
    elif ans == ("3"):
      startingPt()
    elif ans == ("4"):
      inventory()
      roseGarden()
    elif ans == ("5"):
      instructions()
      roseGarden()
    else:
      print("\nPlease try again")
      roseGarden()
  else:
    print("\nThe Rose Garden has already been completed")
    startingPt()

def mushroomField():
  if "mf" not in tasks:
    luna.hideturtle()
    bg("mF.png", 700, 525)
    print("\nLuna is at the Mushroom Field, here are her options:")
    print("1. Talk to the Card Soldier")
    print("2. Pluck the mushrooms")
    print("3. Go back")
    print("4. Check inventory")
    print("5. Check instructions")
    ans = input("What should Luna do? Choose between (1-5): ")
    if ans == ("1"):
      print("\nAs Luna goes up to the Card Soldier, he runs straight to her and quickly says, 'hey, you're the human who fell into Wonderland right? You're also here to help with maintenance correct? Word travels fast around here. I can help you with the task here, just trade the red paint and paintbrush with me and I'll give you the 'Mystifying Mushrooms' book to help you identify the poisonous mushrooms you'll need to weed out.'")
      if "Red Paint and Paintbrush" in luna_inventory:
        luna_inventory.remove("Red Paint and Paintbrush")
        cards_inventory.append("Red Paint and Paintbrush")
        cards_inventory.remove("'Mystifying Mushrooms'")
        luna_inventory.append("'Mystifying Mushrooms'")
        print("\nLuna has traded the 'Red Paint and Paintbrush' for the 'Mystifying Mushrooms' book")
      elif "'Mystifying Mushrooms'" in luna_inventory:
        print("\nThe 'Red Paint and Paintbrush' has already been traded for the 'Mystifying Mushrooms' book")
      else:
        print("\nObtain the 'Red Paint and Paintbrush' to trade for the 'Mystifying Mushrooms' book")
      input("Press any key to continue")
      mushroomField()
    elif ans == ("2"):
      if "'Mystifying Mushrooms'" not in luna_inventory:
        print("\nYou don't have the 'Mystifying Mushrooms' book, try asking the Card Soldier for help")
        mushroomField()
      else:
        print("\nLuna opens the 'Mystifying Mushrooms' book and begins reading the list for the poisonous mushrooms, it reads:\n1. Red with white dots\n2. White with black diamonds\n3. Thundercloud\n4. Pink with light pink drizzle\n5. Yellow with blue star\nNote: Please pluck with caution! Pluck from the beginning of the list and go down")
        input("\nPress any key to continue")
        print("\nWhich one should Luna pluck first?")
        num = input("Choose between 1-10: ")
        if num == "1":
          bg("mushroom1.png", 700, 525)
          print("You plucked the poisonous mushroom!")
          num = input("\nChoose between 2-10: ")
        else:
          repluck()
        if num == "4":
          bg("mushroom2.png", 700, 525)
          print("You plucked the poisonous mushroom!")
          num = input("\nChoose between 2, 3, or 5-10: ")
        else:
          repluck()
        if num == "6":
          bg("mushroom3.png", 700, 525)
          print("You plucked the poisonous mushroom!")
          num = input("\nChoose between 2, 3, 5, 7-10: ")
        else:
          repluck()
        if num == "9":
          bg("mushroom4.png", 700, 525)
          print("You plucked the poisonous mushroom!")
          num = input("\nChoose between 2, 3, 5, 7, 8, or 10: ")
        else:
          repluck()
        if num == "10":
          bg("mushroom5.png", 700, 525)
          print("\nYou've completed the Mushroom Field")
          input("Press any key to continue")
          tasks.append("mf")
          lastPt()
        else:
           repluck()
    elif ans == ("3"):
      lastPt()
    elif ans == ("4"):
      inventory()
      mushroomField()
    elif ans == ("5"):
      instructions()
      mushroomField()
    else:
      print("\nPlease try again")
      mushroomField()
  else:
    print("\nThe Mushroom Field has already been completed")
    lastPt()

def teaParty():
  if "tp" not in tasks:
    luna.hideturtle()
    bg("tP.png", 700, 525)
    print("\nLuna is at the Tea Party, here are her options:")
    print("1. Talk to the Card Soldier")
    print("2. Talk to the Mad Hatter")
    print("3. Go back")
    print("4. Check inventory")
    print("5. Check instructions")
    ans = input("What should Luna do? Choose between (1-5): ")
    if ans == ("1"):
      print("\nAs Luna goes up to the Card Soldier, he looks at you eagerly and whispers, 'I've been waiting for you... Wonderland thanks you for your service!' he bows, 'you must be here to deal with the Mad Hatter... I have some 'Mad Hatter Information' to trade with you for the 'Mystifying Mushrooms' book.'")
      if "'Mystifying Mushrooms'" in luna_inventory:
        luna_inventory.remove("'Mystifying Mushrooms'")
        cards_inventory.append("'Mystifying Mushrooms'")
        cards_inventory.remove("Mad Hatter Information")
        luna_inventory.append("Mad Hatter Information")
        print("\nLuna has traded the 'Mystifying Mushrooms' book for the 'Mad Hatter Information'")
      elif "Mad Hatter Information" in luna_inventory:
        print("\nThe 'Mystifying Mushrooms' book has already been traded for the 'Mad Hatter Information'")
      else:
        print("\nObtain the 'Mystifying Mushrooms' book to trade for the 'Mad Hatter Information'")
      input("Press any key to continue")
      teaParty()
    elif ans == ("2"):
      if book in luna_inventory:
        print("\nThe Mad Hatter looks at Luna with a sparkle in his eyes and ushers her to sit down at the table. She obliges and sits down. He says, 'Welcome! I see that you have a unique book with you... '" + book + "', is it? What do you think about trading that book with me? I'll give you my 'Mad Hat'. What does it do? That's for me to know and for you to find out! So, what do you say?'" )
        print("\nLuna decides to trade the book and obtains the 'Mad Hat'")
        madh_inventory.remove("Mad Hat")
        luna_inventory.append("Mad Hat")
        luna_inventory.remove(book)
        madh_inventory.append(book)
        input("Press any key to continue")
        bg("fire.png", 700, 525)
        print("\n'Perfect! Here's my hat!'\nAs soon as Luna touches the fabric of the hat, she feels a force overcome herself and she puts the hat onto her head. The Mad Hatter laughs hysterically and says, 'It worked! I'll be able to take over Wonderland with her,' he then looks directly at Luna, 'you're going to be my pawn in destroying Wonderland... that old hag has been in power for far too long. It's time for a new era... the Madlands will rise!' But Luna couldn't hear him, her eyes are lifeless as fire spreads throughout the area and excuriating screams can be heard all over...")
        print("\nYou have obtained the Alternate Ending: The Destruction of Wonderland")
      else:
        if "Mad Hatter Information" not in luna_inventory:
          print("\nYou don't have information on the Mad Hatter, try asking the Card Soldier for help")
          teaParty()
        else:
          print("\nThe 'Mad Hatter Information' states:\nThe Mad Hatter is a picky person who is very particular about his teacups. Since his favorite color is blue, he won't allow anyone but himself to use the blue-colored teacups. Even going so far as to putting poison (that only he is immune to) in all of his blue-colored cups to prevent others from using them.")
          input("\nPress any key to continue")
          print("\nThe Mad Hatter looks at you with knowing eyes and says, 'Welcome to my mAd TeA pArTy Luna! Oh, are you wondering why I know your name? Of course I'd know! You're the talk of Wonderland recently, the hot new issue! You're doing maintenance for the Queen... And one of the tasks is to shut me up right? Well, I'll make you a deal. There are currently three tea cups in front of you, two of them are poisoned and one of them is safe. If you can pick the correct tea to drink then I'll stop having so many loud parties. Well then... pick your poison...'")
          choosing = True
          while choosing:
            print("\nThree cups are lined up in a row in front of Luna:")
            print("1. Red cup with blue swirls")
            print("2. Blue cup with yellow stars")
            print("3. Yellow cup with red hearts")
            ans = input("Which one should she choose between 1-3?\n")
            if ans == "3":
              print("\nAs Luna drinks from the teacup, a light and fruity floral flavor greets her tastebuds. She finishes the drink feeling refreshed and the Mad Hatter claps his hands slowly.\n'Congrats! You chose the correct teacup! I guess the information you obtained from that Card Soldier was useful after all...' with a bitter look on his face he continues, 'as promised, I'll keep quiet from now on... pass my regards to the Queen.'")
              choosing = False
              tasks.append("tp")
              input("Press any key to continue")
              startingPt()
            elif ans == "1" or ans == "2":
              print("\nAs Luna drinks from the teacup, she feels a little lightheaded and collapses to the ground. The Mad Hatter can be heard laughing menacingly as the world around her goes dark...")
              print("\nYou have obtained the Bad Ending: The Poisonous Demise")
              choosing = False
            else:
              print("\nPlease try again")
    elif ans == ("3"):
      startingPt()
    elif ans == ("4"):
      inventory()
      teaParty()
    elif ans == ("5"):
      instructions()
      teaParty()
    else:
      print("\nPlease try again")
      teaParty()
  else:
    print("\nThe Mad Hatter's Tea Party has already been completed")
    startingPt()

def heartsCastle():
  if "rg" and "mf" and "tp" in tasks:
    luna.hideturtle()
    bg("hC.png", 700, 402)
    print("\nLuna is at the Hearts Castle, here are her options:")
    print("1. Talk to the Card Soldier")
    print("2. Play croquet with the Queen")
    print("3. Go back")
    print("4. Check inventory")
    print("5. Check instructions")
    ans = input("What should Luna do? Choose between (1-5): ")
    if ans == ("1"):
      print("\nAs Luna goes up to the Card Soldier, he looks at her with excitement.\n'Hello! You're here to play croquet with the Queen correct? Trade the 'Mad Hatter Information' with me to get the 'Stiff Flamingo. You can use it as a mallet to play croquet.'")
      if "Mad Hatter Information" in luna_inventory:
        luna_inventory.remove("Mad Hatter Information")
        cards_inventory.append("Mad Hatter Information")
        cards_inventory.remove("Stiff Flamingo")
        luna_inventory.append("Stiff Flamingo")
        print("\nLuna has traded the 'Mad Hatter Information' for a 'Stiff Flamingo")
      elif "Stiff Flamingo" in luna_inventory:
        print("\nThe 'Mad Hatter Information' has already been traded for a 'Stiff Flamingo'")
      else:
        print("\nObtain the 'Mad Hatter Information' to trade for the 'Stiff Flamingo'")
      input("Press any key to continue")
      heartsCastle()
    elif ans == ("2"):
      if "Stiff Flamingo" not in luna_inventory:
        print("\nYou don't have a croquet club, try asking the Card Soldier for help")
        heartsCastle()
      else:
        print("\nThe Queen looks at you judgingly, 'so you've finally arrived... I've heard of your achievements, they are quite commendable. You wish to go back to Earth correct?'\nLuna nods.\nThe Queen continues, 'well, take this match of croquet as the last test for me to see if you are deserving of such an honor. If you can answer all three of my questions correctly then you can start of the match, but you'll only have so many tries to answer my questions... so answer carefully.")
        ans = input("\n'How many flowers did you paint in the Rose Garden?\n")
        if ans == "5":
          print("\n'Correct, onto the next question.'")
          ans = input("\nHow many total mushrooms were in the Mushroom Field?\n")
        else:
          zeroHealth()
        if ans == "10":
          print("\n'Correct, onto the last question.'")
          ans = input("\nWhat is the Mad Hatter's favorite color? (type in all lowercase letters)\n")
        else:
          zeroHealth()
        if ans == "blue":
          print("\n'Correct, you may start the match.'")
          print("\nLuna starts off the croquet match and lands an overwhelming win against the Queen. The Queen is impressed with her skill and leads Luna to a large door. The Queen unlocks the door and a white light blinds Luna, she close her eyes and goes through the door")
          bg("black.png", 700, 515)
          input("\nPress any key to continue")
          bg("lake.png", 700, 519)
          print("\nLuna opens her eyes and sees the blue lake and colorful flowers of her frontyard. She has finally made it home")
          print("\nYou have obtained the Good Ending: Finally Home")
        else:
          zeroHealth()
    elif ans == ("3"):
      middlePt()
    elif ans == ("4"):
      inventory()
      heartsCastle()
    elif ans == ("5"):
      instructions()
      heartsCastle()
    else:
      print("\nPlease try again")
      heartsCastle()
  else:
    print("\nLuna hasn't finished all three of her tasks yet. The Queen has seen her...")
    if "Silver Pocket Watch" not in luna_inventory:
      heartHealth()
      if health == 0:
        print("\nLuna has lost all her hearts, she has become the Queen's slave")
        print("\nYou have obtained the Bad Ending: The Heartless Soul")
      else:
        middlePt()
    else:
      luna_inventory.remove("Silver Pocket Watch")
      print("\nThe 'Silver Pocket Watch' has prevented one heart from being stolen\nLuna has " + str(health) + " hearts left")
      middlePt()

def repaint():
  print("\nLuna painted in the wrong order, talk to the Card Soldier to find out the correct order")
  input("Press any key to continue")
  roseGarden()

def repluck():
  print("\nLuna plucked the wrong mushroom, reread the 'Mystifying Mushrooms' book to identify the poisonous mushrooms")
  input("Press any key to continue")
  mushroomField()

def heartHealth():
  global health
  health = health - 1
  print("\nLuna has lost one heart, she has " + str(health) + " heart(s) left. If her heart(s) go down to zero, the game will end")

def zeroHealth():
  if "Silver Pocket Watch" not in luna_inventory:
    heartHealth()
    if health == 0:
      print("\nLuna has lost all her hearts, she has become the Queen's slave")
      print("\nYou have obtained the Bad Ending: A Heart's Slave")
    else:
      print("You've answered incorrectly, please try again")
      heartsCastle()
  else:
      luna_inventory.remove("Silver Pocket Watch")
      print("\nThe 'Silver Pocket Watch' has prevented one heart from being stolen\nLuna has " + str(health) + " hearts left")
      print("You've answered incorrectly, please try again")
      heartsCastle()

def pos(x, y):
  luna.showturtle()
  luna.goto(x, y)

def bg(pic, x, y):
  wn.bgpic(pic)
  wn.setup(x, y)
  wn.update()

def inventory():
  print("\nThe items in Luna's inventory are:")
  for item in (luna_inventory):
    print(item)
  input("\nPress any key to continue")

def instructions():
  print("\nThe White Rabbit's instructions state:\n1. Go to the Rose Garden and paint the white roses red\n2. Go to the Mushroom Field and weed out the poisonous mushrooms\n3. Go to the Mad Hatter's Tea Party and shut him up\n4. Go to the Hearts Castle and meet with the Queen\nNotes:\na. Do NOT in any circumstances, meet the Queen before you finish the first 3 steps (you'll lose one heart)\nb. The Card Soldiers at each location might be able to help you with each task")
  input("\nPress any key to stop reading")
#------------------Functions--------------------------------

playing = True
while playing:
  wn = turtle.Screen()
  luna = turtle.Turtle()
  luna.color("hotpink")
  luna.pensize(10)
  luna.shape("circle")
  luna.penup()

  health = 3
  luna_inventory = []
  wr_inventory = ["Silver Pocket Watch"]
  madh_inventory = ["Mad Hat"]
  cards_inventory = ["Red Paint and Paintbrush", "'Mystifying Mushrooms'", "Mad Hatter Information", "Stiff Flamingo"]
  tasks = []
  
  bg("lake.png", 700, 519)
  luna.hideturtle()

  print("\nIt is a warm and sunny day with bright blue skies. A house sits still, surrounded by vibrant and blooming flowers. Luna is seated across from this view, in her favorite spot underneath the dark shade of the oak tree, she is currently reading...\n")

  book = input("Input a title for the book Luna is reading: ")
  print("Luna has obtained '" + book + "'")

  luna_inventory.append(book)

  print("\n" + "She finishes '" + book + "' just as a strong breeze blows by. She looks up and sees a peculiar sight, a white rabbit wearing a royal red tailcoat with golden buttons and a white button-up standing upright with a gleaming golden pocket watch in its paw. Alice looks in shock as the rabbit opens its mouth and speaks with fluent English. 'I’m late, I’m late!' It says. The rabbit then goes on all fours and dashes away. Luna, full of curiosity, follows after the rabbit.\n")

  input("Press any key to continue\n")
  bg("black.png", 700, 515)

  print("Suddenly she loses her footing and falls into an unseen hole. 'What the!? I’m falling!' She shouts in horror as she begins free-falling. She closes her eyes shut as she braces for the hard landing, but it never came. Instead, she was met with a surprisingly soft and pillowly-like surface.\n")

  input("Press any key to continue\n")
  bg("wL.png", 700, 525)

  print("When Luna opens her eyes to check her surroundings, she is greeted by cards swirling in the sky. On closer inspection, she also sees a floating teapot in the sky pouring tea into teacups. Luna is then met with the realization that she is not on Earth anymore, as this place is way too bizarre to exist in real life.\n") 

  input("Press any key to continue\n")

  print("'Hey you!' A familiar voice can be heard. She looks around and sees no one.\n'Oi, down here!' Luna looks down and sees the prim and proper white rabbit adjusting his mini red bowtie. 'Did you follow me all the way down here?'\n'Huh, down?' Luna replies, visibly confused.\n'Yeah, you’re down in Wonderland,' he analyzes her appearance and continues, 'look, you shouldn’t be here. If the Queen finds out that you've snuck into her kingdom, she might just go off with your head.'\n") 

  input("Press any key to continue\n")

  print("Horrified, Luna asks the rabbit if there is any way for her to go back home to Earth. The rabbit says that if maybe Luna were to do some maintenance in the Wonderland, the Queen will let her go home. He brings out a piece of paper and a feather ink and quill and begins writing something.\n'I've written down the order in which you should fix things, and the step by step on how to do it as well. Read it over before you begin.")

  instructions()

  print("\n'Also, I may or may not have something that can help you on your journey. It's not for free of course, I'll need something from you too... how about that book you have in your pocket? I've never seen it before... '" + book + "',is it? It looks interesting, I'll give you my 'Silver Pocket Watch' if you give me that book. My 'Silver Pocket Watch' can help you once in preventing a heart from being stolen by the Queen, it will immediately be used up if you come in contact with her. So? What do you say?'")

  working = True
  while working:
    print("\nWhat should Luna do?")
    print("1. Trade the book")
    print("2. Keep the book")
    ans = input("Choose between 1 or 2: ")
    if ans == "1":
      print("\n'Wise decision', the rabbit smiles as he paws over the 'Silver Pocket Watch'\nLuna has gained a 'Silver Pocket Watch'")
      wr_inventory.remove("Silver Pocket Watch")
      luna_inventory.remove(book)
      wr_inventory.append(book)
      luna_inventory.append("Silver Pocket Watch")
      working = False
    elif ans == "2":
      print("\nThe rabbit frowns as he says, 'well, it's your loss'.")
      working = False
    else:
      print("\nPlease try again")
  input("Press any key to continue")
  print("\n'Tread carefully. By the way, the name's White Rabbit. Good luck on your journey.' After saying this, White Rabbit swiftly hops away and leaves Luna all alone in the middle of Wonderland.")

  startingPt()

  reply = input("\nWould you like to replay the game to experience the other endings (y/n)?")
  if reply == "n":
    playing = False
    print("\nThanks for playing!")
  else:
    print("\nLet's go again!")
