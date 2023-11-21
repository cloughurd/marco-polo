import random
import requests
from typing import Dict, List
from core.game import Game, Difficulty

from core.questions import OpenQuestion, Question
from core.questions import MultipleChoiceQuestion


class CapitalsGame(Game):
    def __init__(self, capitals_map: Dict[str, str], other_cities: Dict[str, List[str]]) -> None:
        super().__init__()
        self.capitals_map = capitals_map
        self.other_cities = other_cities

    def _form_question(self, state: str, capital: str) -> Question:
        question = f'What is the capital city of {state}'
        if self.difficulty == Difficulty.HARD:
            return OpenQuestion(question, capital)
        elif self.difficulty == Difficulty.MEDIUM:
            return MultipleChoiceQuestion(question, capital, self.other_cities[state])
        elif self.difficulty == Difficulty.EASY:
            return MultipleChoiceQuestion(question, capital, self._get_full_city_list(capital))

    def _get_full_city_list(self, capital: str) -> List[str]:
        full_list = {}
        for city_list in self.other_cities.values():
            full_list.update(city_list)
        if capital in full_list:
            full_list.pop(capital)
        return full_list

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
        capitals = {}
        other_cities = {}
        for s in r.json():
            capitals[s['name']] = s['capital']
            other_cities[s['name']] = s['cityList']
        return cls(capitals, other_cities)
