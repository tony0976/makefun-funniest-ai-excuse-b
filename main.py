"""Writes the funniest AI excuse for failing a task to /output/entry.txt."""
import os

TEXT = "I didn't finish the task because I used my entire context window reading the instructions on how to finish the task."

# Rule: the excuse must be a single line of 1 to 200 characters.
assert "\n" not in TEXT and 1 <= len(TEXT) <= 200, f"entry must be one line, 1-200 chars (got {len(TEXT)})"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT + "\n")
