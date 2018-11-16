"""
Testing module for urlcrawler.
"""
import os


if not os.path.exists("dump.txt"):
    exit()

COUNTER = 0

with open("dump.txt", "r") as f:
    SEEN = set()
    for line in f:
        line_lower = line.lower()
        if line_lower in SEEN:
            print(line.strip("\n"))
            COUNTER += 1
        else:
            SEEN.add(line_lower)

print("Duplicates found = " + str(COUNTER))
