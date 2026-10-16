from wordle_solver.interfaces.checker import Checker

class AutomaticChecker(Checker):
  def __init__(self, correct: str):
    self.correct: str = correct

  def check(self, guessed: str) -> list[str]:
    alps: set[str] = {*self.correct, *guessed}
    positions_correct: dict[str, set[int]] = {c: {*[]} for c in alps}
    positions_guessed: dict[str, set[int]] = {c: {*[]} for c in alps}

    for i, c in enumerate(self.correct):
      positions_correct[c].add(i)

    for i, c in enumerate(guessed):
      positions_guessed[c].add(i)

    y: list[int] = []
    g: list[int] = []
    r: list[int] = []

    for c in alps:
      overlap = positions_correct[c] & positions_guessed[c]
      ignored = positions_correct[c] - positions_guessed[c]
      useless = positions_guessed[c] - positions_correct[c]
      useless = sorted([*ignored])[len(ignored):]
      pending = sorted([*ignored])[:len(ignored)]
      y.extend([*pending])
      g.extend([*overlap])
      r.extend([*useless])

    result = [' '] * len(self.correct)

    for yi in y:
      result[yi] = 'Y'

    for gi in g:
      result[gi] = 'G'

    for ri in r:
      result[ri] = 'R'

    return result

