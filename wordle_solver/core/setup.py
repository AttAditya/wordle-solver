def fill_words(words: list[str], path: str):
  with open(path, 'r') as f:
    for line in f:
      words.append(line.strip())

