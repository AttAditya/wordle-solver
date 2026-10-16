from random import random

from wordle_solver.interfaces.guesser import Guesser

class WeightedErroredCharsGuesser(Guesser):
  def guess(
    self,
    pending_words: list[str],
    guesses: list[str]
  ) -> str:
    if len(guesses) < 1:
      return "slate"

    alps = "qwertyuioplkjhgfdsazxcvbnm"
    weights = {c: 0.0 for c in alps}

    for word in pending_words:
      for c in {*word}:
        weights[c] += 1

    max_weight = sum(weights.values())
    min_weight = 0

    for c in weights:
      offset = 1
      shifted = weights[c] - min_weight
      downscale = max_weight - min_weight + offset
      weights[c] = shifted / downscale

    weights['a'] **= 2
    weights['e'] **= 2
    weights['i'] **= 2
    weights['o'] **= 2
    weights['u'] **= 2
    best = (float('-inf'), '')

    for word in pending_words:
      weight = sum(weights[c] for c in {*word})
      weight += random() * 0.1

      if weight > best[0]:
        best = (weight, word)

    return best[1]

