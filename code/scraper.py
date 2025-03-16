import sqlite3
import requests
from bs4 import BeautifulSoup
from bs4 import SoupStrainer

def get_player_stats(soup:BeautifulSoup, team:str):
    pass


if __name__ == '__main__':
    URL = 'https://www.naturalstattrick.com/game.php?season=20242025&game=20001'
    r = requests.get(URL)
    s = BeautifulSoup(r.content, 'html.parser', parse_only=SoupStrainer(class_="tev datadiv"))
    print(s("tbody")[1])
    