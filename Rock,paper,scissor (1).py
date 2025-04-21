import random
from enum import Enum
from dataclasses import dataclass

class Move(Enum):
    ROCK = '🪨 Rock'
    PAPER = '📄 Paper'
    SCISSORS = '✂️ Scissors'

    @staticmethod
    def from_input(choice: str):
        mapping = {'r': Move.ROCK, 'p': Move.PAPER, 's': Move.SCISSORS}
        return mapping.get(choice.lower())

    def __str__(self):
        return self.value

@dataclass
class Player:
    name: str

    def make_move(self) -> Move:
        while True:
            choice = input(f"{self.name}, choose (r/p/s): ")
            move = Move.from_input(choice)
            if move:
                return move
            print("❌ Invalid choice. Try again.")

class Game:
    def __init__(self):
        self.user = Player("You")
        self.computer = Player("Computer")

    def decide_winner(self, user_move: Move, comp_move: Move) -> str:
        wins = {
            Move.ROCK: Move.SCISSORS,
            Move.PAPER: Move.ROCK,
            Move.SCISSORS: Move.PAPER,
        }

        if user_move == comp_move:
            return "🤝 It's a tie!"
        elif wins[user_move] == comp_move:
            return "🎉 You win!"
        else:
            return "💻 Computer wins!"

    def play(self):
        print("🎮 Welcome to Rock-Paper-Scissors!")
        while True:
            user_move = self.user.make_move()
            comp_move = random.choice(list(Move))
            print(f"\n🧍 You chose: {user_move}")
            print(f"🤖 Computer chose: {comp_move}")

            result = self.decide_winner(user_move, comp_move)
            print(f"\n🏁 Result: {result}")

            if input("\n🔁 Play again? (y/n): ").lower() != 'y':
                print("👋 Thanks for playing!")
                break

if __name__ == "__main__":
    Game().play()
