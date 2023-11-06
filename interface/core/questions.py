import random
from typing import List


class Question:
    def __init__(self, question: str, answer: str) -> None:
        self.question = question
        self.answer = answer

    def eval(self, response: str) -> bool:
        return response.lower() == self.answer.lower()

class OpenQuestion(Question):
    def __init__(self, question: str, answer: str) -> None:
        super().__init__(question, answer)

    def __str__(self) -> str:
        return f'{self.question}?'

class MultipleChoiceQuestion(Question):
    def __init__(self, question: str, answer: str, options: List[str], count: int = 4) -> None:
        super().__init__(question, answer)
        self.count = count
        self.options = options
        self.choices = self._create_choices()

    def _create_choices(self) -> List[str]:
        answer_placement = random.randint(0, self.count - 1)
        choices = random.sample(self.options, self.count - 1)
        choices.insert(answer_placement, self.answer)
        return choices

    def __str__(self) -> str:
        q = f'{self.question}?'
        for idx in range(len(self.choices)):
            q += f'\n\t{idx}. {self.choices[idx]}'
        return q

    def eval(self, response: str) -> bool:
        if super().eval(response):
            return True
        try:
            return super().eval(self.choices[int(response)])
        except ValueError:
            return False
