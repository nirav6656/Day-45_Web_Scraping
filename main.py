from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(response.content,"html.parser")

movie_list = []
movie_title = soup.find_all(name="h3",class_="title")
print(movie_title)
for movie in movie_title:
    movie_list.append(movie.getText())
print(movie_list)

with open("movie.txt",mode="w") as data:
    for movie in reversed(movie_list):
        data.write(f"{movie} \n")
