"""Lab 2
Christian Doss
Main file of lab 2 for the game logic
9/27/2026"""


from player import Player

def main():
    print("This is the Coin Match Game!\n")

    player1 = Player("Jeremiah")
    player2 = Player("Brock")

    print("Do you want to toss each coin?\nYes or No?")

    playing = input()

    while playing == "Yes":
        print(f'{player1.get_name()} has {player1.get_wallet()} coins\n{player2.get_name()} has {player2.get_wallet()} coins\n')

        player1.toss_coin()
        player2.toss_coin()

        player1_coin = player1.get_coin_side()
        player2_coin = player2.get_coin_side()

        print(f'{player1.get_name()} flipped {player1_coin}\n{player2.get_name()} tossed {player2_coin}\n')

        if player1_coin == player2_coin:
            print(f'The coins Matched!\n{player1.get_name()} wins 1 coin!\n')
            player1.update_wallet(1)
            player2.update_wallet(-1)
        else:
            print(f'The coins do not Match!\n{player2.get_name()} wins 1 coin!\n')
            player1.update_wallet(-1)
            player2.update_wallet(1)

        if player1.get_wallet() <= 0 or player2.get_wallet() <=0:
            break

        print("Do you want to toss each coin?\nYes or No?\n")

        playing = input()

    print(f'Final Score\n{player1.get_name()} has {player1.get_wallet()} coin(s)\n{player2.get_name()} has {player2.get_wallet()} coin(s)')

    if player1.get_wallet() > player2.get_wallet():
        print(f'{player1.get_name()} wins The Coin Match Game!')
    else:
        print(f'{player2.get_name()} wins The Coin Match Game!')

if __name__ == "__main__":
    main()