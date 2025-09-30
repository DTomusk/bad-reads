from abc import ABC, abstractmethod

from better_profanity import profanity


class AbstractProfanityService(ABC):
    @abstractmethod
    def string_contains_profanity(self, text: str) -> bool:
        pass

class ProfanityService(AbstractProfanityService):
    def __init__(self):
        profanity.load_censor_words()

    def string_contains_profanity(self, text: str) -> bool:
        return profanity.contains_profanity(text)
