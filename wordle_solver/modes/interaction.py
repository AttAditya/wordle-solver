from wordle_solver.checkers.manual import ManualChecker
from wordle_solver.core.main import simulate
from wordle_solver.interfaces.guesser import Guesser
from wordle_solver.interfaces.mode import Mode

class InteractionMode(Mode):
  def __init__(self, words: list[str], guesser: Guesser):
    self.words = words
    self.guesser = guesser
    self.checker = ManualChecker()

  def run(self):
    simulate(
      self.words,
      self.checker,
      self.guesser,
      user_notes=True,
    )

