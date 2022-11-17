import sys
from random import randint

GAME_WIDTH = 10
GAME_HEIGHT = 10

diamont_x = randint(0,GAME_WIDTH)
diamont_y = randint(0, GAME_HEIGHT)
knife_x = randint(0,GAME_WIDTH)
knife_y = randint(0,GAME_WIDTH)


player_x = 0
player_y = 0
player_found_diamont = False
player_found_knife = False
start_player = True



print('diament', diamont_x, diamont_y)
print('nóż', knife_x, knife_y)

while start_player:
    action = input(' Witaj ! Możesz poruszać się w kierunkach określonych jako [W/A/S/D], kliknij enter aby zacząć, lub q aby wyjść :)  :   ')
    match action.lower():
        case 'q':
            quit()
        case '':
            break


while not player_found_diamont and not player_found_knife:

    move = input(' Dokąd idziesz? ')
    match move.lower():
        case 'w':
            player_y+= 1
            if player_y > GAME_HEIGHT:
                print('ałaa!')
                player_y = GAME_HEIGHT
        case 's':
            player_y-= 1
            if player_y < 0:
                print('ałaa!')
                player_y = GAME_HEIGHT
                player_y = 0
        case 'a':
            player_x+= 1
            if player_x > GAME_WIDTH:
                print('ałaa!')
                player_x = GAME_WIDTH
        case 'd':
            player_x-= 1
            if player_x < 0:
                print('ałaa!')
                player_x = GAME_WIDTH
                player_x = 0
        case 'q':
            quit()
        case '':
            print('Nie wiem dokąd idziesz..')
            continue

    if player_x == diamont_x and player_y == diamont_y:
        print('Znalazłeś diament!')
        quit()

    if player_x == knife_x and player_y == knife_y:
        print('umarłeś! koniec gry')

#nastepny etap dodanie ilosci zyc, np 5 zyc, po wyczerpaniu zzakonczenie gry...



    print(player_x, player_y)
