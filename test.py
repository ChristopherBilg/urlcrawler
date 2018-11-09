"""
Testing module for urlcrawler.
"""
counter = 0

with open("dump.txt") as f:
    seen = set()
    for line in f:
        line_lower = line.lower()
        if line_lower in seen:
            print(line.strip("\n"))
            counter += 1
        else:
            seen.add(line_lower)

print("Duplicates found = " + str(counter))
