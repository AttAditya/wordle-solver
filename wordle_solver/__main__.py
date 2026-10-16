from wordle_solver.core.engine import run_cli
from wordle_solver.core.setup import fill_words

if __name__ == "__main__":
  path = "words.txt"
  words: list[str] = []
  fill_words(words, path)
  run_cli(words)

