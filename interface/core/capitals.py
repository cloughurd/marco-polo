import random
import requests
from typing import Dict
from core.game import Game, Difficulty

from core.questions import OpenQuestion, Question


class CapitalsGame(Game):
    def __init__(self, capitals_map: Dict[str, str], *, difficulty: Difficulty = Difficulty.HARD) -> None:
        super().__init__(difficulty=difficulty)
        self.capitals_map = capitals_map

    def _form_question(self, state: str, capital: str) -> Question:
        question = f'What is the capital city of {state}'
        if self.difficulty == Difficulty.HARD:
            return OpenQuestion(question, capital)
        elif self.difficulty == Difficulty.MEDIUM:
            # TODO:
            pass
        elif self.difficulty == Difficulty.EASY:
            # TODO:
            pass

    def __iter__(self):
        shuffled = list(self.capitals_map.items())
        random.shuffle(shuffled)
        for state, capital in shuffled:
            yield self._form_question(state, capital)

    def __len__(self):
        return len(self.capitals_map)

    @classmethod
    def build_game(cls, url: str):
        r = requests.get(f'{url}/states')
        print(r.json())
        capitals = {}
        for s in r.json():
            capitals[s['name']] = s['capital']
        return cls(capitals)
