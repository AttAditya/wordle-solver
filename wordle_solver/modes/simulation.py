from wordle_solver.checkers.automatic import AutomaticChecker
from wordle_solver.core.main import simulate
from wordle_solver.interfaces.guesser import Guesser
from wordle_solver.interfaces.mode import Mode

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

