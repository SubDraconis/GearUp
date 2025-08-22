# GearUp: Menedżer Sprzętu ASG

## O Projekcie

TacticLoad to projekt stworzony z myślą o pasjonatach Airsoftu, który ma na celu ułatwienie planowania i optymalizacji wyposażenia. Aplikacja, zbudowana w oparciu o framework Flask w języku Python, pozwala użytkownikom na wirtualne "skompletowanie" swojego sprzętu, od broni po umundurowanie. Dzięki temu gracze mogą z łatwością kontrolować wagę swojego ekwipunku, zarządzać budżetem i eksperymentować z różnymi konfiguracjami przed dokonaniem zakupu czy wyjściem w teren. Projekt jest rozwijany z naciskiem na prostotę obsługi i modularność.

## Główne Funkcje

* Przeglądanie rozbudowanego asortymentu w podziale na kategorie i podkategorie.
* Dynamiczne dodawanie i usuwanie przedmiotów z ekwipunku.
* Interaktywny, chowany "plecak" do podglądu wybranego sprzętu.
* Automatyczne obliczanie na żywo łącznej wagi i ceny wyposażenia.
* Podział aplikacji na stronę główną oraz podstronę "Sklep".

## Zastosowane Technologie

* **Backend:** Python, Flask
* **Frontend:** HTML, CSS (Flexbox), JavaScript
* **Zarządzanie stanem:** Sesje po stronie serwera (Flask Session)

## Jak Uruchomić Projekt

1.  Upewnij się, że masz zainstalowany Python oraz bibliotekę Flask (`pip install Flask`).
2.  Sklonuj repozytorium na swój komputer.
3.  W głównym folderze projektu (`stonaweb`) uruchom aplikację za pomocą komendy w terminalu:
    ```bash
    python app.py
    ```
4.  Otwórz przeglądarkę internetową i wejdź na adres `http://127.0.0.1:5000`.