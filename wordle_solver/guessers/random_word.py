from random import choice

from wordle_solver.interfaces.guesser import Guesser

class RandomWordGuesser(Guesser):
  def guess(
    self,
    pending_words: list[str],
    guesses: list[str]
  ) -> str:
    return choice(pending_words)

