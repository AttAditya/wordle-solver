files_count = int(input())
failed: dict[int, int] = {}
solved: dict[int, int] = {}

for _ in range(files_count):
  failed_count = int(input())

  for _ in range(failed_count):
    score, count = map(int, input().split())

    if score not in failed:
      failed[score] = 0

    failed[score] += count

  solved_count = int(input())

  for _ in range(solved_count):
    score, count = map(int, input().split())

    if score not in solved:
      solved[score] = 0

    solved[score] += count

print("Failed")
print(len(failed))

for score in sorted(failed.keys()):
  print(score, failed[score])

print("Solved")
print(len(solved))

for score in sorted(solved.keys()):
  print(score, solved[score])

