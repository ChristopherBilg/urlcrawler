"""
Crawl module.
"""
import os
import search as Search


def scan_links(webpage, maximum, filename):
    """
    Main function to itterate. (needs a rewrite)
    """
    links_indexed = [webpage]
    links_visited = []
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
                    if counter % 2500 == 0:
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


if __name__ == "__main__":
    scan_links("https://en.wikipedia.org", 2000000, "dump.txt")
