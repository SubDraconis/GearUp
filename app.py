import os
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'a-default-secret-key-for-development-only')

# --- DANE APLIKACJI (Bez zmian) ---
ASORTYMENT = {
    "Broń": {
        'Karabiny': [
            {'nazwa': 'M4A1', 'cena': 1200, 'waga': 3.1},
            {'nazwa': 'AK-74', 'cena': 1100, 'waga': 3.3},
            {'nazwa': 'G36', 'cena': 1350, 'waga': 3.6}
        ],
        'Pistolety': [
            {'nazwa': 'Glock 17', 'cena': 600, 'waga': 0.9},
            {'nazwa': 'Beretta M9', 'cena': 650, 'waga': 0.95},
            {'nazwa': 'Desert Eagle', 'cena': 800, 'waga': 2.0}
        ],
        'Snajperki': [
            {'nazwa': 'AWM', 'cena': 1800, 'waga': 6.5},
            {'nazwa': 'Barrett M82', 'cena': 3500, 'waga': 14.0},
            {'nazwa': 'SVD Dragunov', 'cena': 1600, 'waga': 4.3}
        ]
    },
    "Wyposażenie": {
        'Kamizelki': [
            {'nazwa': 'Kamizelka taktyczna Plate Carrier', 'cena': 350, 'waga': 2.5},
            {'nazwa': 'Kamizelka typu Chest Rig', 'cena': 200, 'waga': 1.1},
            {'nazwa': 'Pas taktyczny z szelkami', 'cena': 180, 'waga': 0.9}
        ],
        'Hełmy': [
            {'nazwa': 'Hełm typu FAST', 'cena': 250, 'waga': 1.5},
            {'nazwa': 'Hełm typu MICH 2000', 'cena': 220, 'waga': 1.6},
            {'nazwa': 'Pokrowiec na hełm w kamuflażu', 'cena': 50, 'waga': 0.2}
        ],
        'Ochrona twarzy i oczu': [
            {'nazwa': 'Gogle balistyczne', 'cena': 150, 'waga': 0.3},
            {'nazwa': 'Okulary ochronne', 'cena': 80, 'waga': 0.1},
            {'nazwa': 'Maska stalowa typu Stalker', 'cena': 60, 'waga': 0.2}
        ],
        'Umundurowanie': [
            {'nazwa': 'Spodnie bojówki', 'cena': 250, 'waga': 0.8},
            {'nazwa': 'Bluza mundurowa', 'cena': 220, 'waga': 0.9},
            {'nazwa': 'Koszulka termoaktywna', 'cena': 90, 'waga': 0.3}
        ],
        'Obuwie': [
            {'nazwa': 'Buty taktyczne wysokie', 'cena': 450, 'waga': 1.8},
            {'nazwa': 'Buty trekkingowe niskie', 'cena': 350, 'waga': 1.2},
            {'nazwa': 'Ochraniacze na buty (stuptuty)', 'cena': 70, 'waga': 0.4}
        ],
        'Plecaki': [
            {'nazwa': 'Plecak taktyczny 25L', 'cena': 180, 'waga': 1.2},
            {'nazwa': 'Plecak szturmowy 40L', 'cena': 280, 'waga': 1.9},
            {'nazwa': 'Torba zrzutowa na magazynki', 'cena': 50, 'waga': 0.3}
        ]
    }
}
WSZYSTKIE_PRZEDMIOTY_LOOKUP = {
    item['nazwa']: item 
    for grupa_kategorii in ASORTYMENT.values() 
    for kategoria in grupa_kategorii.values() 
    for item in kategoria
}

# --- NOWA FUNKCJA POMOCNICZA ---
def _pobierz_kontekst_dla_szablonu():
    """Pobiera ekwipunek z sesji, oblicza statystyki i zwraca jako słownik."""
    ekwipunek_raw = session.get('ekwipunek', [])
    
    # Zabezpieczenie przed starymi danymi w sesji
    ekwipunek = [item for item in ekwipunek_raw if isinstance(item, dict)]
    if len(ekwipunek) != len(ekwipunek_raw):
        session['ekwipunek'] = ekwipunek
        session.modified = True

    return {
        "kategorie": ASORTYMENT,
        "moj_ekwipunek": ekwipunek,
        "laczna_waga": round(sum(item.get('waga', 0) for item in ekwipunek), 2),
        "laczna_cena": sum(item.get('cena', 0) for item in ekwipunek)
    }

# --- GŁÓWNE WIDOKI (TRASY) ---

@app.route('/')
def strona_glowna():
    """Wyświetla stronę główną."""
    kontekst = _pobierz_kontekst_dla_szablonu()
    return render_template('main.html', **kontekst)

@app.route('/sklep')
def strona_sklep():
    """Wyświetla stronę sklepu."""
    kontekst = _pobierz_kontekst_dla_szablonu()
    return render_template('sklep.html', **kontekst)

# --- AKCJE (Dodawanie/Usuwanie) ---

@app.route('/dodaj', methods=['POST'])
def dodaj_przedmiot():
    """Dodaje przedmiot do ekwipunku w sesji."""
    nazwa_przedmiotu = request.form.get('nazwa_przedmiotu')
    przedmiot_do_dodania = WSZYSTKIE_PRZEDMIOTY_LOOKUP.get(nazwa_przedmiotu)
    
    if przedmiot_do_dodania:
        ekwipunek = session.get('ekwipunek', [])
        ekwipunek.append(przedmiot_do_dodania)
        session['ekwipunek'] = ekwipunek
        session.modified = True
    
    # Przekierowujemy z powrotem do strony, z której przyszło żądanie (np. ze sklepu do sklepu)
    return redirect(request.referrer or url_for('strona_glowna'))

@app.route('/usun', methods=['POST'])
def usun_przedmiot():
    """Usuwa przedmiot z ekwipunku na podstawie jego indeksu."""
    index_do_usuniecia_str = request.form.get('index_przedmiotu')
    
    if 'ekwipunek' in session and index_do_usuniecia_str is not None:
        try:
            index = int(index_do_usuniecia_str)
            if 0 <= index < len(session['ekwipunek']):
                session['ekwipunek'].pop(index)
                session.modified = True
        except (ValueError, IndexError):
            pass # Ignorujemy błędne żądania
            
    return redirect(request.referrer or url_for('strona_glowna'))

if __name__ == '__main__':
    app.run(debug=True)