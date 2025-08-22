# Cele i Plan Rozwoju Projektu TacticLoad

Ten plik zawiera listę potencjalnych ulepszeń i nowych funkcji, które mogą zostać dodane do projektu w przyszłości.

---

### ## Etap 1: Natychmiastowe Ulepszenia (Poprawa tego, co już mamy)

* [ ] **Wiadomości "Flash" dla Użytkownika:** Dodać powiadomienia (np. "Dodano M4A1") po dodaniu/usunięciu przedmiotu przy użyciu systemu `flash` z Flaska.
* [ ] **Przycisk "Wyczyść Ekwipunek":** Dodać przycisk w plecaku, który usuwa wszystkie przedmioty z sesji.
* [ ] **Licznik Przedmiotów na Ikonie Plecaka:** Dodać małą cyfrę na ikonie 🎒, która pokazuje, ile przedmiotów jest aktualnie w ekwipunku.
* [ ] **Ulepszone Przekierowania:** Sprawić, by po dodaniu/usunięciu przedmiotu użytkownik wracał na stronę, na której był (np. na `/sklep`), a nie zawsze na stronę główną.
* [ ] **Dokończenie Nawigacji:** Zaimplementować podstrony dla linków "Wyposażenie" i "Kontakt" w menu.

---

### ## Etap 2: Średniozaawansowane Funkcje (Nowe Możliwości)

* [ ] **Obrazki dla Przedmiotów:** Dodać do każdego przedmiotu pole z linkiem do obrazka i wyświetlać te obrazki w sklepie.
* [ ] **Sortowanie i Filtrowanie:** Dodać na stronie sklepu opcje sortowania (po cenie, wadze) i pole do filtrowania przedmiotów po nazwie.
* [ ] **Osobne Strony dla Kategorii:** Stworzyć dedykowane podstrony dla głównych kategorii (np. `/bron` i `/wyposazenie`).
* [ ] **Szczegółowe Strony Przedmiotów:** Umożliwić kliknięcie na przedmiot, aby przejść do osobnej strony z jego szczegółowym opisem i większym zdjęciem.
* [ ] **Porównywanie Przedmiotów:** Dodać funkcję zaznaczenia kilku przedmiotów i wyświetlenia ich statystyk w tabeli porównawczej.

---

### ## Etap 3: Zaawansowane Rozszerzenia (Profesjonalizacja Aplikacji)

* [ ] **Integracja z Bazą Danych (np. SQLite):** Przenieść cały asortyment z pliku `app.py` do bazy danych.
* [ ] **Panel Administratora:** Stworzyć zabezpieczoną hasłem podstronę do zarządzania asortymentem w bazie danych (dodawanie/edycja/usuwanie przedmiotów).
* [ ] **Konta Użytkowników:** Dodać system rejestracji i logowania.
* [ ] **Zapisywanie Skompletowanych Zestawów:** Umożliwić zalogowanym użytkownikom zapisywanie swoich konfiguracji na stałe na ich koncie.
* [ ] **Stworzenie API:** Przebudować aplikację do architektury API-first, gdzie Flask dostarcza tylko dane (JSON), a frontend jest budowany w JavaScripcie.
* [ ] **Testy Automatyczne:** Napisać testy jednostkowe i integracyjne, aby zapewnić stabilność aplikacji przy wprowadzaniu nowych zmian.
