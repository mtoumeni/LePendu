# -*-coding:Latin-1 -*

import os
import random
from fonctions import*

current_directory = os.getcwd()
os.chdir(current_directory)
number_of_points = {}
lucky_number = 0
rule = True
found_text = ""
character_fruits = []
continue_game = True

text_information = '''\nBienvenue au jeu du pendu. 
Le principe est simple: il s'agit de deviner le nom du fruit
qui a ete choisi dans une liste.\n
Vous devez entrer une lettre a chaque fois.
Si la lettre se trouve dans le nom du fruit, elle sera affichee a l'ecran et,
le nombre de chances restant ne sera pas decremente
les lettres non trouvees seront masquees par des asterix *****. \n
Vous aurez droit a 10 essais.\n'''

print(text_information)
player_name = str (input("Enter your player name: "))

while continue_game:
     list_characters_found = []
     list_characters_already_used = []
     number_of_points = read_score(player_name)
     display_score(player_name,number_of_points)

    # We retrieve the number of chances from the file
     with open('words_list.txt', 'r') as words_list:
         text = words_list.readlines()
         for elt in text:                                             
            if elt.strip() == '10':
              lucky_number = int(elt)                        
              break
          
        # The fruit to guess is chosen
         while rule:
              chosen_index = random.randrange(len(text)-1)
              genre_typ =(text[chosen_index])
              if len(genre_typ) == 2:
                continue                    
              else:
                  break

     fruit_name = text[chosen_index].lower().strip()
     while lucky_number >0 and found_text != fruit_name:
          found_text = ""
          count = False
          print(f"Your remaining number of chances is: {lucky_number} \n")     
          character_fruits = input("Enter a letter: ")          
          if character_fruits in list_characters_already_used or character_fruits in list_characters_found :
            print("You have already entered this letter")              
          elif character_fruits not in list_characters_found:
            if character_fruits in fruit_name:
              list_characters_found.append(character_fruits)
              count = True  
            else:
              list_characters_already_used.append(character_fruits)   

          for i in fruit_name:
            if i in list_characters_found:
              found_text += i          
            else:
                  found_text += "*"

          print(f"{found_text} \n")
          if not count:  
            lucky_number -= 1

     if found_text == fruit_name:
       print("Congratulations, you won the game!")
     else:
       print(f"The correct answer was ***{fruit_name}*** ")
       print("You lost the game!")
       lucky_number = 0

     print("You have finished the game with:",lucky_number, "points" )	
     save_score(player_name,lucky_number,number_of_points)
     letter = input("Do you want to continue the game (Y/N) ?: ").lower()
     if letter == "n":
       continue_game = False
     else:
         continue_game

print("Goodbye and see you soon..." )	