import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
movies_data = soup.find_all(name="h3", class_="title")

movies_titles = [movie.getText() for movie in movies_data]
movies_titles.reverse()

open("movies.txt", mode="w")
with open("movies.txt", mode="w") as file:
    for title in movies_titles:
        file.write(f"{title}\n")





