from bs4 import BeautifulSoup
# import lxml
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")
# a = article.getText("")
movie_titles = [title.text for title in all_movies]
movie_titles.reverse()
# print(movies)
# print(type(movies))
with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in movie_titles:
        file.write(f"{movie}\n")
