import requests
import json

def get_movie(movie_title):
    api_key = "f583f8ef"
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        movie_data = json.loads(response.text)
        return movie_data
    else:
        return None

def main():
    movie_title = input("Введите название фильма: ")
    movie_info = get_movie(movie_title)

    if movie_info:
        print("Информация о фильме", movie_title)
        print("Название:", movie_info.get("Title"))
        print("Год выпуска:", movie_info.get("Year"))
        print("Режиссер:", movie_info.get("Director"))
        print("Описание:",movie_info.get("Plot"))
    else:
        print("Фильм не найден или произошла ошибка")

if __name__ == "__main__":
    main()

        
        
