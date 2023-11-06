from enum import Enum


class Difficulty(Enum):
    HARD = 3
    MEDIUM = 2
    EASY = 1

class Game:
    def __init__(self, difficulty: Difficulty) -> None:
        self.difficulty = difficulty

    @classmethod
    def build_game(cls, url: str):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

class Round:
    def __init__(self, game: Game) -> None:
        self.game = game
        self.num_questions = len(game)
        self.num_correct = 0

    def get_score(self):
        return self.num_correct / self.num_questions

    def play(self):
        for question in self.game:
            print(question)
            response = input('\nAnswer: ')
            if question.eval(response):
                self.num_correct += 1
        print(f'\n***Congratulations! Your score is {self.get_score():.2%}***\n')
