from sys import argv

from wordle_solver.guessers.weighted_chars import WeightedCharsGuesser
from wordle_solver.interfaces.mode import Mode
from wordle_solver.modes.evaluation import EvaluationMode
from wordle_solver.modes.interaction import InteractionMode
from wordle_solver.modes.simulation import SimulationMode

def run_cli(words: list[str]):
  if len(argv) < 2:
    print("Usage: python wordle.py <mode>")
    return

  selected_mode = argv[1]
  guesser = WeightedCharsGuesser()
  mode = Mode()

  if selected_mode == "-p":
    picked = None

    if len(argv) < 3:
      picked = input("Enter the picked word: ")
    else:
      picked = argv[2]

    mode = SimulationMode(
      words,
      picked,
      guesser,
    )

  if selected_mode == "-i":
    mode = InteractionMode(
      words,
      guesser,
    )

  if selected_mode == "-e":
    start = None
    end = None

    if len(argv) >= 4:
      start = int(argv[2])
      end = int(argv[3])

    mode = EvaluationMode(
      words,
      guesser,
      start,
      end
    )

  mode.run()

