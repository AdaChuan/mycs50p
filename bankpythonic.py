# PART 1 — the reusable tool (always loaded, always available)
def classify_greeting(greeting: str) -> str:
    greeting = greeting.lower().strip()

    if greeting.startswith("hello"):
        return "$0"
    elif greeting.startswith("h"):
        return "$20"
    return "$100"

# PART 2 — the "run this as a script" block (only runs if directly executed)
if __name__ == "__main__":
    greeting = input("What's your greeting? ")
    print(classify_greeting(greeting))

# Under the hood:
# You type: python greet.py
#                 ↓
# Terminal hands "greet.py" to the OS
#                 ↓
# OS finds the Python interpreter and says
# "run this file as the MAIN program"
#                 ↓
# CPython sees it's the MAIN program
# and sets __name__ = "__main__"
#                 ↓
# Your code runs
