from dataclasses import dataclass
from typing import Generic, TypeVar


T = TypeVar("T")

@dataclass
class Failure:
    error: str
    code: int = 400

@dataclass
class Outcome(Generic[T]):
    isSuccess: bool
    data: T = None
    failure: Failure = None