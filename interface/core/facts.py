import random
from typing import List
import requests

from interface.core.game import Game, Difficulty
from interface.core.questions import OpenQuestion, Question

class StateFactsGame(Game):
    def __init__(self, states: List[str], url: str) -> None:
        super().__init__()
        self.states = states
        self.url = url

    def _form_question(self, state: str) -> Question:
        if self.difficulty == Difficulty.HARD:
            r = requests.get(f'{self.url}/state/{state.lower()}/fact')
            fact = r.json()['message']
            return OpenQuestion(f'{fact}\nFor which state is that a true fact', state)
        raise NotImplementedError

    def __iter__(self):
        shuffled = self.states.copy()
        random.shuffle(shuffled)
        for state in shuffled:
            yield self._form_question(state)

    def __len__(self):
        return len(self.states)

    @classmethod
    def build_game(cls, url: str):
        r = requests.get(f'{url}/states?includeCities=false')
        states = r.json()
        return cls(states, url)
