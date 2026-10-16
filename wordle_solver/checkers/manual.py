from wordle_solver.interfaces.checker import Checker

class ManualChecker(Checker):
  def _validate(self, feedback: str) -> bool:
    if len(feedback) != 5:
      print("Feedback must be 5 characters long.")

      return False

    if not all(c in "GYR" for c in feedback):
      print("Feedback must only contain G, Y, or R.")

      return False

    return True

  def _request(self, guessed: str) -> str:
    result = input(f"Feedback for {guessed}: ")
    result = result.strip().upper()

    if not self._validate(result):
      result = ""

    return result

  def check(self, guessed: str) -> list[str]:
    result = ""

    while not result:
      result = self._request(guessed)

    return [c for c in result.strip()]

