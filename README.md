# Wordle Solver

A Wordle game solver implemented in Python with parallel evaluation capabilities.

## Features

- **Play mode**: Solve a specific Wordle puzzle automatically
- **Interactive mode**: Play Wordle and provide feedback manually
- **Evaluate mode**: Benchmark the solver against a range of words from the dictionary
- **Parallel evaluation**: Run evaluations across multiple processes for speed
- **Letter frequency weighting**: Uses character frequency analysis to rank guesses

## Project Structure

```
wordle_solver/
├── core/           # Core engine, CLI, setup
├── guessers/       # Guessing algorithms
├── checkers/       # Word validation
├── interfaces/     # Interfaces
├── modes/          # Game modes (simulation, interaction, evaluation)
└── __main__.py     # Package entry point
```

| File/Directory | Description |
|----------------|-------------|
| `wordle_solver/` | Main package |
| `helpers/` | Helper scripts (merge, progress) |
| `parallel.sh` | Runs parallel evaluation batches |
| `words.txt` | Word dictionary (~14,855 words) |
| `logs/` | Output directory for evaluation logs |

## Usage

Run the solver using the Python module syntax:

### Solve for a specific word (Simulation mode)
```bash
python3 -m wordle_solver -p <word>
# or provide word when prompted:
python3 -m wordle_solver -p
```

### Play interactively
```bash
python3 -m wordle_solver -i
```

### Evaluate solver performance
```bash
# Evaluate words 0-1000
python3 -m wordle_solver -e 0 1000

# Run parallel evaluation (default: 15000 words, step 500)
./parallel.sh

# Custom limits
./parallel.sh <limit> <step> <start_num>
```

## Algorithm

The solver uses a frequency-based heuristic:
1. Calculate letter weights based on frequency in remaining candidates
2. Score each candidate word by sum of unique letter weights
3. Pick highest-scoring word as next guess
4. Filter candidates based on Wordle feedback (G=Green, Y=Yellow, R=Red)
5. Repeat until solved or no candidates remain

## Output

Evaluation mode outputs:
- **Solved**: Words guessed correctly with guess count distribution
- **Failed**: Words not solved within the iteration limit

