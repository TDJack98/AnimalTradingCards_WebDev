import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.score = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

    def win(self):
        self.score += 1


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        choice = input("Rock, paper, scissors? > ").lower()
        if (choice != "rock" and choice != "paper" and choice != "scissors"
           and choice != "quit"):
            return self.move()
        else:
            return choice


class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()
        self.p1move = ""
        self.p2move = ""

    def move(self):
        if self.p1move != "":
            return self.p2move
        else:
            return random.choice(moves)

    def learn(self, my_move, their_move):
        self.p1move = my_move
        self.p2move = their_move


class CyclePlayer(ReflectPlayer):
    def move(self):
        if self.p1move == "rock":
            return "paper"
        elif self.p1move == "paper":
            return "scissors"
        elif self.p1move == "scissors":
            return "rock"
        else:
            return random.choice(moves)


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        if move1 == "quit":
            self.end_game()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2):
            print("** PLAYER ONE WINS **")
            self.p1.win()
        elif move1 == move2:
            print("** TIE **")
        else:
            print("** PLAYER TWO WINS **")
            self.p2.win()
        print(f"Score: Player One {self.p1.score}, Player Two {self.p2.score}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("This is the game rock, scissors, paper.")
        print("Choose one of them or 'quit' to leave the game.")
        print("Game start!")
        round = 0
        while True:
            print(f"Round {round + 1}:")
            self.play_round()
            round += 1
        print("Game over!")

    def end_game(self):
        print(f"The final score is Player One {self.p1.score}, "
              f"Player Two {self.p2.score}.")
        if self.p1.score > self.p2.score:
            winner = 1
        elif self.p1.score < self.p2.score:
            winner = 2
        else:
            winner = 0
            print("It's a tie.")
            exit()
        print(f"The Winner is Player {winner}!")
        exit()


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
