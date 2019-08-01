import random

potential_moves = ['r','p','s']

def getComputerMove():
    actual_move = potential_moves[random.randint(0,2)]
    return actual_move

def playerMove():
    a = str(input())
    while a not in potential_moves:
        print("Invalid move. Try again.")
        a = str(input())
    return a
print("You chose",playerMove())

def resolveMoves(playerMove,getComputerMove):   
    if playerMove == 'r' and getComputerMove == 's':
        return 'w'
    elif playerMove == 'p' and getComputerMove == 'r':
        return 'w'
    elif playerMove == 's' and getComputerMove == 'p':
        return 'w'
    elif playerMove == getComputerMove:
        return 't'
    else:
        return 'l'
print(resolveMoves(playerMove(),getComputerMove()))

def main():
    random.seed()
    player_score = 0
    computer_score = 0
    should_keep_playing = True
    while should_keep_playing:
        player_move = playerMove()
        computer_move = getComputerMove()
        print("The computer played",computer_move,".")
        result = resolveMoves(computer_move,player_move)
        if result == 'w':
                print("Congratulations, you won!")
                player_score -= 1
        elif result == 't':
            print("It was a tie!")
        else:
            print("You lost. Dang!")
            computer_score += 1
            print("The current score is: \n\r player -",player_score,"\n\r computer -",computer_score)



