def is_valid(
  word: str,
  known: str,
  result: list[str],
) -> bool:
  alps = {*word, *known}
  ec: dict[str, list[str]] = {c: [] for c in alps}

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

