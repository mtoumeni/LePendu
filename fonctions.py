# -*-coding:Latin-1 -*

import os
import pickle


current_directory = os.getcwd()
os.chdir(current_directory)

def read_score(player_name):
   player_score = {}
   try:
       with open('scores', 'rb') as scores:
           scores.read()
   except IOError:              
                  player_score[player_name] = "0"
                  with open('scores', 'wb') as scores:
                      my_pickler = pickle.Pickler(scores)
                      my_pickler.dump(player_score)
                      return player_score
   else:
        if os.path.getsize("../LePendu/scores") > 0: 
          with open('scores', 'rb') as scores:
              my_depickler = pickle.Unpickler(scores)
              player_score = my_depickler.load()
              if player_name in player_score.keys():                    
                return player_score
              else:
                   with open('scores', 'wb') as scores:
                       player_score[player_name] = "0"
                       my_pickler = pickle.Pickler(scores)
                       my_pickler.dump(player_score)
                       return player_score

# The player's score is displayed before the game begins
def display_score(player_name,list_score):
   if player_name in list_score:
     print("{} Your score is {}: \n".format(player_name, list_score[player_name]))

# The player's score is recorded at the end of the game
def save_score(player_name,chances_remaining,list_score):   
   if os.path.getsize("../LePendu/scores") > 0: 
     with open('scores', 'rb') as list_score:
         my_depickler = pickle.Unpickler(list_score)
         recovered_score = my_depickler.load()
         if player_name in recovered_score.keys():
            recovered_score[player_name] = int(recovered_score[player_name])
            recovered_score[player_name] = recovered_score[player_name] + chances_remaining
            print("{} Your recorded score is {}: \n".format(player_name, recovered_score[player_name]))
      
   if os.path.getsize("../LePendu/scores") > 0: 
     with open('scores', 'wb') as list_score:
         my_pickler = pickle.Pickler(list_score)
         my_pickler.dump(recovered_score)



























