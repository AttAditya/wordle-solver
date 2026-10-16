from checkers.automatic import AutomaticChecker

from core.main import simulate

from interfaces.guesser import Guesser
from interfaces.mode import Mode

class SimulationMode(Mode):
  def __init__(
    self,
    words: list[str],
    picked: str,
    guesser: Guesser,
  ):
    self.words = words
    self.picked = picked
    self.guesser = guesser
    self.checker = AutomaticChecker(picked)

  def run(self):
    guesses = simulate(
      self.words,
      self.checker,
      self.guesser,
      user_notes=False,
    )

    print("Guesses:", len(guesses))
    print(*guesses, sep="\n")

