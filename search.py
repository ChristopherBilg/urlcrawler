#!usr/bin/env python3
"""
Search module.
"""
import requests as Requests
from bs4 import BeautifulSoup


class Search:
    """
    Class to searching a web page and getting retrieving data.
    """
    def __init__(self, webpage):
        """
        Initialization method.
        """
        self.webpage = webpage

    def get_links(self):
        """
        Get all href links on self.webpage
        """
        try:
            request = Requests.get(self.webpage)
        except Requests.exceptions.RequestException as e:
            print(e)
            return []

        data = request.text
        soup = BeautifulSoup(data, "html.parser")

        all_links_found = []

        for link in soup.find_all("a"):
            if link.has_attr("href"):
                href = str(link.get("href"))

                if href == "/":
                    pass

                if href.startswith("/"):
                    while href.startswith("//"):
                        href = href[1:]
                    all_links_found.append(self.webpage + href)
                elif href.startswith("http"):
                    all_links_found.append(href)

        return all_links_found
