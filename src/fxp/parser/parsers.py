import os
import json
import pickle
import requests
from bs4 import BeautifulSoup as BS
from abc import ABC, abstractmethod

from fxp.parser import DEFAULT_USER_AGENT, HOST, PREVIEW_URL, BASE_DIR


class BaseParser(ABC):
    def __init__(self, user_agent: str = None):
        self._user_agent = user_agent if user_agent is not None else DEFAULT_USER_AGENT

    def _get_page(self, url):
        response = requests.get(
            url,
            headers={
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code == 200:
            return BS(response.text)
        raise ValueError("Response not 200")

    @abstractmethod
    def save_to_file(self, name: str) -> None:
        """Save news to file

        :param name: file name
        :type name: str
        """

    @abstractmethod
    def save_to_json(self, name: str) -> None:
        """Save news to json file

        :param name: file name
        :type name: str
        """


class Preview(BaseParser):
    def __init__(self, **kwargs):
        super().__init__(kwargs.get("user_agent"))
        self.__num_page = kwargs.get("page") or 1
        self.__links = []

    def get_links(self):
        try:
            html = self._get_page(PREVIEW_URL.format(HOST, self.__num_page))
        except ValueError:
            self.__links = []
        else:
            box = html.find("div", attrs={"class": "largeTitle"})
            if box is not None:
                articles = box.find_all(
                    "article", attrs={"class": "js-article-item articleItem"}
                )
                for article in articles:
                    link = article.find("a", attrs={"class": "title"})
                    self.__links.append(HOST + link.get("href"))
            else:
                self.__links = []

    def save_to_file(self, name):
        path = os.path.join(BASE_DIR, name + ".bin")
        pickle.dump(self.__links, open(path, "wb"))

    def save_to_json(self, name):
        path = os.path.join(BASE_DIR, name + ".json")
        json.dump(self.__links, open(path, "w"))


if __name__ == "__main__":
    parser = Preview(page=2)
    parser.get_links()
    print(parser._Preview__links)
    parser.save_to_json("links_2")
    parser.save_to_file("links_2")