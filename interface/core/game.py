from distutils import core
from enum import Enum


class Difficulty(Enum):
    HARD = 3
    MEDIUM = 2
    EASY = 1

class Game:
    def __init__(self, difficulty: Difficulty = Difficulty.HARD) -> None:
        self.difficulty = difficulty

    @classmethod
    def build_game(cls, url: str):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

class Round:
    def __init__(self, game: Game, difficulty: Difficulty) -> None:
        self.game = game
        self.set_difficulty(difficulty)
        self.num_questions = len(game)
        self.num_correct = 0

    def get_score(self) -> float:
        return self.num_correct / self.num_questions

    def set_difficulty(self, difficulty: Difficulty) -> None:
        self.game.difficulty = difficulty

    def play(self) -> None:
        for question in self.game:
            print(question)
            correct = None
            while correct is None:
                response = input('\nAnswer: ')
                try:
                    correct = question.eval(response)
                except Exception:
                    print('Not a valid response, try again...')
            if correct:
                self.num_correct += 1
        print(f'\n***Congratulations! Your score is {self.get_score():.2%}***\n')
