"""
Crawl module.
"""
import os
import search as Search


links_indexed = []
links_visited = []


def scan_links(webpage, maximum, filename, modulus):
    """
    Main function to itterate. (needs a rewrite)
    """
    links_indexed.append(webpage)
    counter = 1

    while links_indexed:
        for link in links_indexed:
            links_indexed.remove(link)
            links_visited.append(link)

            for href in Search.Search(link).get_links():
                if href in links_indexed or href in links_visited:
                    pass
                else:
                    links_indexed.append(href)
                    counter += 1
                    if counter % modulus == 0:
                        print(str(counter)
                              + " | " + str(len(links_indexed))
                              + " | " + str(len(links_visited)))

            if counter >= maximum and maximum != -1:
                break
        if counter >= maximum and maximum != -1:
            break

    if os.path.exists(filename):
        os.remove(filename)
    with open(filename, "w") as file_:
        for link in links_indexed:
            file_.write(link + "\n")
        file_.write("\n")
        for link in links_visited:
            file_.write(link + "\n")


if __name__ == "__main__":
    try:
        scan_links("https://en.wikipedia.org", 1000000, "dump.txt", 1000)
    except KeyboardInterrupt:
        if os.path.exists("dump.txt"):
            os.remove("dump.txt")
        with open("dump.txt", "w") as file_:
            for link in links_indexed:
                file_.write(link + "\n")
            file_.write("\n")
            for link in links_visited:
                file_.write(link + "\n")
