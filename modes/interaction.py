from checkers.manual import ManualChecker

from core.main import simulate

from interfaces.guesser import Guesser
from interfaces.mode import Mode

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

