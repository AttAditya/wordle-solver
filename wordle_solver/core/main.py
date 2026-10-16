from wordle_solver.core.validator import is_valid
from wordle_solver.interfaces.checker import Checker
from wordle_solver.interfaces.guesser import Guesser

def simulate(
  words: list[str],
  checker: Checker,
  guesser: Guesser,
  user_notes: bool = False,
) -> list[str]:
  guesses: list[str] = []

  while len(words) > 1:
    if not words:
      if user_notes:
        print("No valid words left.")

      break

    guessed = guesser.guess(words, guesses)
    result = checker.check(guessed)
    guesses.append(guessed)
    new_words: list[str] = []

    for word in words:
      if is_valid(word, guessed, result):
        new_words.append(word)

    words = new_words

  if words:
    guesses.append(words[0])

  unique_guesses: set[str] = {*[]}
  result: list[str] = []

  for guessed in guesses:
    if guessed not in unique_guesses:
      unique_guesses.add(guessed)
      result.append(guessed)

  if user_notes:
    print("No valid words left.")

  return result

