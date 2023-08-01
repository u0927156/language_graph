# %% Imports
import requests
from bs4 import BeautifulSoup
import pathlib

# %%
URL = "https://ilibrary.ru/text/11/p.1/index.html"
page = requests.get(URL)
# %%

soup = BeautifulSoup(page.content, "html.parser")

# %%

spans = soup.find_all("span", class_="p")
# %%

tolstoy_base_path = pathlib.PurePath(".", "data", "RU", "Tolstoy", "WarAndPeace")
file_path = tolstoy_base_path / "Chapter1.txt"
with open(file_path, "w") as f:
    for span in spans:
        f.write(span.text)
        f.write("\n")
# %%
