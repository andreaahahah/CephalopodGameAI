import playingStrategies
#import random
#import game

#E' IL BLU

# The moves of player have the form (x,y), where y is the column number and x the row number (starting with 0)
#h1_alphabeta_search è quello creato da me con h1
def playerStrategy (game,state):
    cutOff = 3 # The depth of the search tree. It can be changed to test the performance of the player.
    # The player uses the alphabeta search algorithm to find the best move.
    value,move = playingStrategies.h1_alphabeta_search(game,state,playingStrategies.cutoff_depth(cutOff))
  
    return move

#TODO forse è utile aumentare il cutOff quando ci avviciniamo alla fine
