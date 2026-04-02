import random


class Die:

    def __init__(self, value=None):
        self._value = value

    def roll(self):
        new_value = random.randint(1, 6)
        self._value = new_value
        # return new_value

    @property
    def value(self):
        return self._value


class Player:

    def __init__(self, die, is_computer=False):
        self._die = die
        self._is_computer = is_computer
        self._counter = 5

    @property
    def die(self):
        return self._die

    @property
    def is_computer(self):
        return self._is_computer

    @property
    def counter(self):
        return self._counter

    def increment_counter(self):
        self.counter += 1

    def decrement_counter(self):
        self.counter -= 1

    def roll_die(self):
        self._die.roll()

    @counter.setter
    def counter(self, value):
        self._counter = value

class DiceGame:

    def __init__(self, player, computer):
        self.player = player
        self.computer =computer

    def play(self):
        print("\n============================")
        print("🎲 Welcome to Dice Dame...🎲 \n  🏆 First to 0 wins...🏆")
        print("============================")

        while True:
            self.play_round()
            game_over = self._check_game_over()
            if game_over:
                break

    def play_round(self):
        # Print welcome message
        self._print_round_welcome()

        # Trigger the rolls first!
        self.player.roll_die()
        self.computer.roll_die()

        # Show values
        self._show_dice_values()

        # Determine winner and loser
        if my_player.die.value > computer_player.die.value:
            print("\n-------- You won the round 🎉 --------\n")
            self._update_counters(winner=self.player, loser=self.computer)
        elif computer_die.value > player_die.value:
            print("\n-------- Computer wins this round 🤕.... Try again --------\n")
            self._update_counters(winner=self.computer, loser=self.player)
        else:
            print("\n-------- It's a tie 🤑 --------\n")

        # Show counters
        self._show_counters()

    def _print_round_welcome(self):
        print("\n---------- New round ----------")
        input("🎲 Press any key to roll the dice 🎲\n")

    def _show_dice_values(self):
        print(f"👨 Your 🎲: {my_player.die.value}")
        print(f"💻 Computer 🎲: {computer_player.die.value}")

    def _update_counters(self, winner, loser):
        winner.decrement_counter()
        loser.increment_counter()

    def _show_counters(self):
        print(f"👨 Your score: {self.player.counter}")
        print(f"💻 Computer score: {self.computer.counter}")

    def _check_game_over(self):
        if self.player.counter == 0:
            self._print_game_over(winner=self.player)
            return True
        elif self.computer.counter == 0:
            self._print_game_over(winner=self.computer)
            return True
        else:
            return False

    def _print_game_over(self, winner):
        print("\n============================")
        print("Game Over...")
        if winner.is_computer:
            if winner.is_computer:
                print("You lose 🤮")
        else:
            if not winner.is_computer:
                print("You win 🏆")
        print("============================")


# create instances
player_die = Die()
computer_die = Die()

my_player = Player(player_die, is_computer=False)
computer_player = Player(computer_die, is_computer=True)

game = DiceGame(my_player, computer_player)
game.play()

