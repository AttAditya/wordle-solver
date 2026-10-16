from wordle_solver.checkers.automatic import AutomaticChecker
from wordle_solver.core.main import simulate
from wordle_solver.interfaces.guesser import Guesser
from wordle_solver.interfaces.mode import Mode

class EvaluationMode(Mode):
  def __init__(
    self,
    words: list[str],
    guesser: Guesser,
    start: int | None = None,
    end: int | None = None,
  ):
    self.words = words
    self.start = start
    self.end = end
    self.guesser = guesser

    if self.start is None:
      self.start = int(input())

    if self.end is None:
      self.end = int(input())

    self.space = self.words[self.start:self.end]

  def run(self):
    failed: dict[int, int] = {}
    solved: dict[int, int] = {}

    for i, picked in enumerate(self.space):
      total = len(self.space)
      progress = 100 * (i + 1) / total
      print(
        f"\rProgress: {progress:.4f}%",
        flush=True, end="",
      )

      checker = AutomaticChecker(picked)
      guesses = simulate(
        self.words,
        checker,
        self.guesser,
      )

      score = len(guesses)
      scores: dict[int, int] = failed

      if guesses[-1] == picked:
        scores = solved

      if score not in scores:
        scores[score] = 0

      scores[score] += 1
      print(
        f"\rSolved: {picked}, Guesses ({score}): {guesses}",
        flush=True, end="\n"
      )

    print("\r")
    print("Failed")
    print(len(failed))

    for score in sorted(failed.keys()):
      print(score, failed[score])

    print("Solved")
    print(len(solved))

    for score in sorted(solved.keys()):
      print(score, solved[score])

