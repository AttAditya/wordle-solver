from random import randint

words = []
pending = 5

def common_letters(word1, word2):
  return ''.join(c for c in word2 if c in word1)

path = "words.txt"
with open(path, 'r') as f:
  for line in f:
    words.append(line.strip())

picked = "fatal".lower()

def is_valid(word, required, forbidden):
  return all(c in word for c in required) and all(c not in word for c in forbidden)

prev_len = len(words)
curr_len = len(words) + 1
count = 0
last_guess = None

while prev_len != curr_len:
  if not words:
    break

  count += 1
  new_words = []
  guess = words[randint(0, len(words) - 1)]

  while guess == last_guess and len(words) > 1:
    guess = words[randint(0, len(words) - 1)]

  last_guess = guess
  keep = common_letters(guess, picked)
  discard = ''.join(c for c in guess if c not in keep)
  pending -= len(keep)

  for word in words:
    if is_valid(word, keep, discard):
      new_words.append(word)

  words = new_words
  prev_len = curr_len
  curr_len = len(words)

print(words, count)

