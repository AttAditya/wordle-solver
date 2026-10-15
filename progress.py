import glob
import os
import re
import time

THRESHOLD = 100
INTERVAL = 0.01
LOG_DIR = "logs"

while True:
  percentages = []

  for path in glob.glob(os.path.join(LOG_DIR, "*")):
    if not os.path.isfile(path):
      continue

    try:
      with open(path, "r", errors="ignore") as f:
        lines = f.readlines()

      for line in reversed(lines):
        matches = re.findall(r"(\d+(?:\.\d+)?)%", line)

        if matches:
          percentages.append(float(matches[-1]))
          break
    except (OSError, PermissionError):
      continue

  if percentages:
    avg = sum(percentages) / len(percentages)
    print(f"\rProgress: {avg:.2f}%", end="\r", flush=True)

    if avg >= THRESHOLD:
      print()
      break

  time.sleep(INTERVAL)

