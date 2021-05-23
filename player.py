class Player:
    def __init__(self, name):
        self.name = name
        self.guesses = list()

    def add_guess(self, val):
        self.guesses.append(val)

    def show_guesses(self):
        return self.guesses
