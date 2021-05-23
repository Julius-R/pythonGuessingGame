from game import Game

def game_init():
    mode = input(f"Which mode would you like to play:"
                 f"[1]-Easy "
                 f"[2]-Medium "
                 f"[3]-Hard ")
    modes = {
        1: "Easy",
        2: "Medium",
        3: "Hard"
    }

    new_game = Game(modes[int(mode)])
    new_game.initialize()


game_init()
