"""
Crawl module.
"""
import os
import search as Search


LINKS_INDEXED = []
LINKS_VISITED = []


def scan_links(webpage, maximum, filename, modulus):
    """
    Main function to itterate. (needs a rewrite)
    """
    LINKS_INDEXED.append(webpage)
    counter = 1

    while LINKS_INDEXED:
        for link in LINKS_INDEXED:
            LINKS_INDEXED.remove(link)
            LINKS_VISITED.append(link)

            for href in Search.Search(link).get_links():
                if href in LINKS_INDEXED or href in LINKS_VISITED:
                    pass
                else:
                    LINKS_INDEXED.append(href)
                    counter += 1
                    if counter % modulus == 0:
                        print(str(counter)
                              + " | " + str(len(LINKS_INDEXED))
                              + " | " + str(len(LINKS_VISITED)))

            if counter >= maximum and maximum != -1:
                break
        if counter >= maximum and maximum != -1:
            break

    if os.path.exists(filename):
        os.remove(filename)
    with open(filename, "w+") as _file:
        for link in LINKS_INDEXED + LINKS_VISITED:
            _file.write(link + "\n")


if __name__ == "__main__":
    try:
        # scan_links("https://en.wikipedia.org", -1, "dump.txt", 1000)
        scan_links("https://www.osha.gov", -1, "dump.txt", 500)
    except KeyboardInterrupt:
        if os.path.exists("dump.txt"):
            os.remove("dump.txt")
        with open("dump.txt", "w+") as dump_file:
            for dump_link in LINKS_INDEXED + LINKS_VISITED:
                dump_file.write(dump_link + "\n")
