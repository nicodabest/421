from random import *
#######################################
#              CONDITIONS             #
#######################################
#             Deux joueurs            #
#                3 dés                #
#             ⚀⚁⚂⚃⚄⚅              #
#          Un pot de 21 jetons        #
#######################################
def nvjoueur (pseudo):
    joueur ={'pseudo' : pseudo, 'des' :  [], 'jetons' :0}
    return joueur

def des (player):
    while not player['des']==[]:
        for de in player['des']:
            player['des'].remove(de)
    
    l = 3 
    i = 0
    while i != l:
        n = randint(1,6)
        player['des'].append(n)
        i = i+ 1 
def pot():
    pot=21
    
def combinaisons(j1,j2):
    if sorted(player['des']) == [1,2,4] 
    #10 jetons
    elif sorted(player['des']) == [1,1,1]
    #7 jetons 
    elif sorted(player['des']) == [6,6,6] or sorted(player['des']) == [1,1,6]:
    #6 jetons 
    elif sorted(player['des']) == [5,5,5] or sorted(player['des']) == [1,1,5]:
    #5 jetons
    elif sorted(player['des']) == [4,4,4] or sorted(player['des']) == [1,1,4]:
    #4 jetons
    elif sorted(player['des']) == [3,3,3] or sorted(player['des']) == [1,1,3]:
    #3 jetons
    elif sorted(player['des']) == [2,2,2] or sorted(player['des']) == [1,1,2]:
    #2 jetons
    elif sorted(player['des']) == [1,2,3] or sorted(player['des']) == [2,3,4] or sorted(player['des']) == [3,4,5] or sorted(player['des']) == [4,5,6]:
    #2 jetons
    else:
    #1 jetons
    pass