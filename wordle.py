from sys import argv

def setup(words, path):
  with open(path, 'r') as f:
    for line in f:
      words.append(line.strip())

def wordle_check(correct, guessed, alps):
  positions_correct = {c: {*[]} for c in alps}
  positions_guessed = {c: {*[]} for c in alps}

  for i, c in enumerate(correct):
    positions_correct[c].add(i)

  for i, c in enumerate(guessed):
    positions_guessed[c].add(i)

  y, g, r = [], [], []

  for c in alps:
    overlap = positions_correct[c] & positions_guessed[c]
    ignored = positions_correct[c] - positions_guessed[c]
    useless = positions_guessed[c] - positions_correct[c]
    useless = sorted([*ignored])[len(ignored):]
    pending = sorted([*ignored])[:len(ignored)]
    y.extend([*pending])
    g.extend([*overlap])
    r.extend([*useless])

  result = [' '] * len(correct)

  for yi in y:
    result[yi] = 'Y'

  for gi in g:
    result[gi] = 'G'

  for ri in r:
    result[ri] = 'R'

  return result

def is_valid(word, known, result, alps):
  ec = {c: [] for c in alps}

  for i, c in enumerate(known):
    if result[i] == 'G' and word[i] != c:
      return False

    if result[i] == 'Y' and word[i] == c:
      return False

    ec[c].append(result[i])

  for c in alps:
    if 'R' not in {*ec[c]}:
      continue

    limit = len(ec[c]) - ec[c].count('R')

    if word.count(c) > limit:
      return False

  return True

def guess_word(pending_words, alps, guesses):
  if len(guesses) < 1:
    return "slate"

  weights = {c: 0 for c in alps}

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
  ranked = []

  for word in pending_words:
    weight = sum(weights[c] for c in {*word})
    ranked.append((weight, word))

  ranked.sort(
    key=lambda x: abs(0.2 - x[0] / 5),
    reverse=True,
  )

  return ranked[-1][1]

def main(words, picked, alps):
  guesses = []

  while len(words) > 1:
    if not words:
      break

    guess = guess_word(words, alps, guesses)
    result = wordle_check(picked, guess, alps)
    guesses.append(guess)
    new_words = []

    for word in words:
      if is_valid(word, guess, result, alps):
        new_words.append(word)

    words = new_words

  if words:
    guesses.append(words[0])

  unique_guesses = {*[]}
  result = []

  for guess in guesses:
    if guess not in unique_guesses:
      unique_guesses.add(guess)
      result.append(guess)

  return result

def evaluate(words, alps, start=None, end=None):
  if start is None:
    start = int(input())

  if end is None:
    end = int(input())

  space = words[start:end]
  failed = {}
  solved = {}

  for i, picked in enumerate(space):
    total = len(space)
    progress = 100 * (i + 1) / total
    print(
      f"\rProgress: {progress:.4f}%",
      flush=True, end="",
    )

    guesses = main(words, picked, alps)
    score = len(guesses)
    scores = failed

    if guesses[-1] == picked:
      scores = solved

    if score not in scores:
      scores[score] = 0

    scores[score] += 1

  print("\r")
  print("Failed")
  print(len(failed))

  for score in sorted(failed.keys()):
    print(score, failed[score])

  print("Solved")
  print(len(solved))

  for score in sorted(solved.keys()):
    print(score, solved[score])

def play(picked, words, alps):
  guesses = main(words, picked, alps)
  print("Guesses:", len(guesses))
  print(*guesses, sep="\n")

def cli():
  if len(argv) < 2:
    print("Usage: python wordle.py <mode>")
    return

  mode = argv[1]

  if mode == "-p":
    picked = None

    if len(argv) < 3:
      picked = input("Enter the picked word: ")
    else:
      picked = argv[2]

    play(picked, words, alps)
    return

  if mode == "-e":
    start = None
    end = None

    if len(argv) >= 4:
      start = int(argv[2])
      end = int(argv[3])

    evaluate(words, alps, start, end)

if __name__ == "__main__":
  alps = "qwertyuioplkjhgfdsazxcvbnm"
  path = "words.txt"
  words = []
  setup(words, path)
  cli()

