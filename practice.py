class TicTacToe:
    def __init__(self):
        self.board = [' ']*10  

    def display_board(self):
        print(f" {self.board[1]} | {self.board[2]} | {self.board[3]} ")
        print("---|---|---")
        print(f" {self.board[4]} | {self.board[5]} | {self.board[6]} ")
        print("---|---|---")
        print(f" {self.board[7]} | {self.board[8]} | {self.board[9]} ")

    def player_input(self, player):
        while True:
            try:
                position = int(input(f"Player '{player}'s turn (1-9): "))
                if 1 <= position <= 9 and self.board[position] == ' ':
                    self.board[position] = player
                    break
                else:
                    print("Invalid move. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def win_check(self, player):
        
        return ((self.board[1] == self.board[2] == self.board[3] == player) or
                (self.board[4] == self.board[5] == self.board[6] == player) or
                (self.board[7] == self.board[8] == self.board[9] == player) or
                (self.board[1] == self.board[4] == self.board[7] == player) or
                (self.board[2] == self.board[5] == self.board[8] == player) or
                (self.board[3] == self.board[6] == self.board[9] == player) or
                (self.board[1] == self.board[5] == self.board[9] == player) or
                (self.board[3] == self.board[5] == self.board[7] == player))

def main():
    game = TicTacToe()
    player = 'X'

    while True:
        game.display_board()
        game.player_input(player)

        if game.win_check(player):
            print(f"Player '{player}' wins!")
            break

        if ' ' not in game.board:
            print("It's a draw!")
            break

        player = 'O' if player == 'X' else 'X'

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y': return
    else: main()

if __name__ == "__main__":
    main()
