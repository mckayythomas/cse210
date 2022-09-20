'''
CSE 210 Assignment: tic-tac-toe
Author: McKay Thomas
'''
def main():
    # give each space a variable to be updated
    a, b, c, d, e, f, g, h, i = 1, 2, 3, 4, 5, 6, 7, 8, 9
    game_over = False
    turn = 0
    print("......TIC......")
    print("......TAC......")
    print("......TOE......")
    print("THREE IN A ROW!")
    print()

    while game_over == False:
        count_turn = True

        make_board(a,b,c,d,e,f,g,h,i)

        # Check if all squares have been used in the case no one will win.
        if turn == 9:
            print("Sorry. Looks like no one wins.\n GAME OVER!!!")
            break

        whose_turn = x_or_o(turn)
        player_choice = input(f"{whose_turn}'s move. Which square would you like to play? (1-9) ")
        print()

        try:
            # Make the players move and update board
            if int(player_choice) == a:
                a = whose_turn
            elif int(player_choice) == b:
                b = whose_turn
            elif int(player_choice) == c:
                c = whose_turn
            elif int(player_choice) == d:
                d = whose_turn
            elif int(player_choice) == e:
                e = whose_turn
            elif int(player_choice) == f:
                f = whose_turn
            elif int(player_choice) == g:
                g = whose_turn
            elif int(player_choice) == h:
                h = whose_turn
            elif int(player_choice) == i:
                i = whose_turn
            else:
                print("Please enter an available space.")
                count_turn = False
        #Handle ValuesError from an empty input from user
        except(ValueError):
            print("Please enter an available space")
            count_turn = False
            
        game_over = winner(a,b,c,d,e,f,g,h,i, whose_turn, game_over)

        if count_turn == True:
            turn += 1

# print the board and game
def make_board(a,b,c,d,e,f,g,h,i):
        print(f"{a} | {b} | {c}")
        print("--+---+--")
        print(f"{d} | {e} | {f}")
        print("--+---+--")
        print(f"{g} | {h} | {i}")
        print()

# determine whose turn it is
def x_or_o(i):
    if i % 2 != 1:
        who = "x"
    else:
        who = "o"
    return who

# determine if there is a winner and the game should end.
def winner(a,b,c,d,e,f,g,h,i, who, game_over):
    if a == who and b == who and c == who:
        make_board(a,b,c,d,e,f,g,h,i)
        print(f"Congradulations {who}'s! You got three in a row!\n YOU WIN!!!")
        game_over = True
    elif a == who and d == who and g == who:
        make_board(a,b,c,d,e,f,g,h,i)
        print(f"Congradulations {who}'s! You got three in a row!\n YOU WIN!!!")
        game_over = True
    elif a == who and e == who and i == who:
        make_board(a,b,c,d,e,f,g,h,i)
        print(f"Congradulations {who}'s! You got three in a row!\n YOU WIN!!!")
        game_over = True
    elif g == who and e == who and c == who:
        make_board(a,b,c,d,e,f,g,h,i)
        print(f"Congradulations {who}'s! You got three in a row!\n YOU WIN!!!")
        game_over = True
    elif d == who and e == who and f == who:
        make_board(a,b,c,d,e,f,g,h,i)
        print(f"Congradulations {who}'s! You got three in a row!\n YOU WIN!!!")
        game_over = True
    elif b == who and e == who and h == who:
        make_board(a,b,c,d,e,f,g,h,i)
        print(f"Congradulations {who}'s! You got three in a row!\n YOU WIN!!!")
        game_over = True    
    elif g == who and h == who and i == who:
        make_board(a,b,c,d,e,f,g,h,i)
        print(f"Congradulations {who}'s! You got three in a row!\n YOU WIN!!!")
        game_over = True
    elif c == who and f == who and i == who:
        make_board(a,b,c,d,e,f,g,h,i)
        print(f"Congradulations {who}'s! You got three in a row!\n YOU WIN!!!")
        game_over = True
    return game_over


if __name__ == '__main__':
    main()