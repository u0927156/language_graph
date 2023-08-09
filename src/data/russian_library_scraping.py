# %% Imports
import requests
from bs4 import BeautifulSoup
import pathlib
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import yaml
import random

# %%

russian_base_path = pathlib.Path("..", "..", "data", "RU")
russian_books_yaml_path = russian_base_path / "russian_books.yaml"

with open(russian_books_yaml_path, "r") as yaml_file:
    books_dictionary = yaml.safe_load(yaml_file)
# %%


def find_foward_nav_element_ilibrary(driver):
    nav_elements = driver.find_elements(By.CLASS_NAME, "navlink")
    for element in nav_elements:
        element_title = element.get_attribute("title")

        if element_title == "Дальше":
            return element

    return None


def write_chapter_to_file(
    soup: BeautifulSoup, curr_book_path: pathlib.Path, chapter_number: int
):
    file_path = curr_book_path / f"Chapter{chapter_number}.txt"

    spans = soup.find_all("span", class_="p")

    with open(file_path, "w") as f:
        for span in spans:
            f.write(span.text)
            f.write("\n")


with webdriver.Chrome() as driver:
    for book in books_dictionary["books"]:
        author = book["author"]
        title = book["title"]
        starting_url = book["starting_url"]

        print(f"Working on {title} by {author}.")

        driver.get(starting_url)

        curr_book_path: pathlib.Path = russian_base_path / author / title
        curr_book_path.mkdir(exist_ok=True, parents=True)

        curr_chapter = 1
        while True:
            if curr_chapter % 25 == 0:
                print(f"Working on Chapter {curr_chapter}")
            soup = BeautifulSoup(driver.page_source, "html.parser")

            write_chapter_to_file(soup, curr_book_path, curr_chapter)
            curr_chapter += 1

            forward_nav_element = find_foward_nav_element_ilibrary(driver)

            if forward_nav_element is not None:
                forward_nav_element.click()
                time.sleep(random.randint(1, 3))
            else:
                break

# %%
