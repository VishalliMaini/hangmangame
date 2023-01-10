import random
word_list=["arkdvark","baboon","camel"]
choosenword=random.choice(word_list)
l=len(choosenword)
print(f"The solution is {choosenword}")
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#creating blank list
n=[]
j=0
no_of_lives=6

for i in range(l):
    n+="_"
    
endgame=False

while not endgame:
    guess=input("guess character").lower()
    for i in range(len(choosenword)):
        if(choosenword[i]==guess):
           
            n[i]=guess
    
    if guess not in choosenword:
        print("guessed Wrong")
        print(stages[no_of_lives])
        no_of_lives=no_of_lives-1
        print(f"You have {no_of_lives} lives left")
    else:
        print(n)
     #if there is no blank left  
    if "_" not in n:
        endgame=True
        print("You Win")
    #if lives are over
    if no_of_lives==0 :
        print("lives are over,You Loss")
        print(stages[no_of_lives])
        break
              
              
