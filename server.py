from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()


class Film(BaseModel):
    id: int
    title: str
    director: str
    year: int


def load_films():
    with open("films.json", "a+", encoding="utf-8") as f:
        f.seek(0)
        text = f.read()

        if text:
            return json.loads(text)

    return []


def save_films(films):
    with open("films.json", "w", encoding="utf-8") as f:
        json.dump(films, f, ensure_ascii=False, indent=4)


@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    films = load_films()

    for film in films:
        if film["id"] == movie_id:
            return film

    return {"Помилка": "Фільм не знайдено"}


@app.post("/movies")
def add_movie(movie: Film):
    films = load_films()

    films.append(movie.dict())

    save_films(films)

    return {"Повідомлення": "Фільм додано"}


@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int):
    films = load_films()

    new_films = []

    deleted = False

    for film in films:
        if film["id"] == movie_id:
            deleted = True
        else:
            new_films.append(film)

    save_films(new_films)

    if deleted:
        return {"Повідомлення": "Фільм видалено"}
    else:
        return {"Помилка": "Фільм не знайдено"}
