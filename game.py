from player import Player
import random


class Game:
    def __init__(self, mode):
        self.mode = mode
        self.number_of_turns = 3
        self.current_turn = 0
        self.winning_number = random.randint(1, 10)
        self.player = Player(input("What should we call you? : "))

    def end_game(self,  did_player_win):
        if did_player_win:
            print(f"Congrats, {self.player.name}! You won.")
        else:
            print(f"Oof, it be like that. Here is the correct answer: {self.winning_number}. Here are your answers: "
                  f"{self.player.show_guesses()}")

    def start_game(self,):
        print(self.winning_number)
        while self.current_turn <= self.number_of_turns:
            if self.current_turn == self.number_of_turns:
                self.end_game(False)
                break
            else:
                player_answer = int(input("What is your guess: "))
                self.player.add_guess(player_answer)
                if player_answer == self.winning_number:
                    self.end_game(True)
                    break
                else:
                    if player_answer < self.winning_number:
                        print("Sorry, your answer is too low")
                    elif player_answer > self.winning_number:
                        print("Sorry, your answer is too high")
                    self.current_turn += 1

    def initialize(self):
        if self.mode == "Easy":
            self.winning_number = random.randint(1, 10)
        elif self.mode == "Medium":
            self.winning_number = random.randint(1, 30)
        else:
            self.winning_number = random.randint(1, 100)
        self.start_game()
