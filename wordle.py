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

def guess_word(pending_words, alps, _):
  weights = {c: 0 for c in alps}

  for word in pending_words:
    for c in {*word}:
      weights[c] += 1

  max_weight = max(weights.values())
  min_weight = min(weights.values())

  for c in weights:
    offset = 1
    shifted = weights[c] - min_weight
    downscale = max_weight - min_weight + offset
    weights[c] = shifted / downscale

  ranked = []

  for word in pending_words:
    weight = sum(weights[c] for c in {*word})
    ranked.append((weight, word))

  ranked.sort()

  return ranked[-1][1]

def main(words, picked, alps):
  prev_len = len(words)
  curr_len = len(words) + 1
  guesses = []

  while prev_len != curr_len:
    if not words:
      break

    new_words = []
    guess = guess_word(words, alps, guesses)

    while guesses and guesses[-1] == guess and len(words) > 1:
      guess = guess_word(words, alps, guesses)

    guesses.append(guess)
    result = wordle_check(picked, guess, alps)

    for word in words:
      if is_valid(word, guess, result, alps):
        new_words.append(word)

    words = new_words
    prev_len = curr_len
    curr_len = len(words)

  return guesses

if __name__ == "__main__":
  alps = "qwertyuioplkjhgfdsazxcvbnm"
  path = "words.txt"
  words = []
  setup(words, path)
  failed = {}
  solved = {}
  space = words

  for i, picked in enumerate(space):
    total = len(space)
    progress = 100 * (i + 1) / total
    print(
      f"\rProgess: {progress:.4f}%",
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

  for score in sorted(failed.keys()):
    print(score, failed[score])

  print("Solved")

  for score in sorted(solved.keys()):
    print(score, solved[score])

