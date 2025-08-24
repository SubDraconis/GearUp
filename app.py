import os
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'a-default-secret-key-for-development-only')

# --- DANE APLIKACJI (Bez zmian) ---
ASORTYMENT = {
    "Broń": {
        'Karabiny': [
            {'nazwa': 'M4A1', 'image_url': 'https://cdn.pixabay.com/photo/2016/11/29/10/37/gun-1868351_1280.jpg', 'cena': 1200, 'waga': 3.1, 'pojemnosc': 350, 'max_rpm': 800},
            {'nazwa': 'AK-74', 'image_url': 'https://cdn.pixabay.com/photo/2016/09/24/04/55/kalashnikov-1691238_1280.jpg', 'cena': 1100, 'waga': 3.3, 'pojemnosc': 500, 'max_rpm': 650},
            {'nazwa': 'G36', 'image_url': 'https://cdn.pixabay.com/photo/2018/06/16/04/18/machine-gun-3477810_1280.jpg', 'cena': 1350, 'waga': 3.6, 'pojemnosc': 470, 'max_rpm': 750}
        ],
        'Pistolety': [
            {'nazwa': 'Glock 17', 'image_url': 'https://cdn.pixabay.com/photo/2018/04/23/15/48/pistol-3343940_1280.jpg', 'cena': 600, 'waga': 0.9, 'pojemnosc': 24, 'max_rpm': 400},
            {'nazwa': 'Beretta M9', 'image_url': 'https://cdn.pixabay.com/photo/2018/06/07/21/22/pistol-3461026_1280.jpg', 'cena': 650, 'waga': 0.95, 'pojemnosc': 23, 'max_rpm': 380},
            {'nazwa': 'Desert Eagle', 'image_url': 'https://cdn.pixabay.com/photo/2018/04/10/21/28/desert-eagle-3309579_1280.jpg', 'cena': 800, 'waga': 2.0, 'pojemnosc': 21, 'max_rpm': 300}
        ],
        'Snajperki': [
            {'nazwa': 'AWM', 'image_url': 'https://cdn.pixabay.com/photo/2018/01/21/04/35/sniper-rifle-3096054_1280.jpg', 'cena': 1800, 'waga': 6.5, 'pojemnosc': 50, 'max_rpm': 50},
            {'nazwa': 'Barrett M82', 'image_url': 'https://cdn.pixabay.com/photo/2018/06/16/04/18/machine-gun-3477810_1280.jpg', 'cena': 3500, 'waga': 14.0, 'pojemnosc': 80, 'max_rpm': 40},
            {'nazwa': 'SVD Dragunov', 'image_url': 'https://cdn.pixabay.com/photo/2018/01/10/02/19/sniper-3072551_1280.jpg', 'cena': 1600, 'waga': 4.3, 'pojemnosc': 60, 'max_rpm': 60}
        ]
    },
    "Wyposażenie": {
        'Kamizelki': [
            {'nazwa': 'Kamizelka taktyczna Plate Carrier', 'image_url': 'https://images.pexels.com/photos/10398363/pexels-photo-10398363.jpeg', 'cena': 350, 'waga': 2.5, 'pojemnosc': 0, 'max_rpm': 0},
            {'nazwa': 'Kamizelka typu Chest Rig', 'image_url': 'https://pixnio.com/free-images/2017/02/22/2017-02-22-19-14-19-1200x799.jpg', 'cena': 200, 'waga': 1.1, 'pojemnosc': 0, 'max_rpm': 0},
            {'nazwa': 'Pas taktyczny z szelkami', 'image_url': 'https://images.unsplash.com/photo-1628173499424-df38d21c4b12', 'cena': 180, 'waga': 0.9, 'pojemnosc': 0, 'max_rpm': 0}
        ],
        'Hełmy': [
            {'nazwa': 'Hełm typu FAST', 'image_url': 'https://pixnio.com/free-images/2017/02/22/2017-02-22-19-12-32-1200x800.jpg', 'cena': 250, 'waga': 1.5, 'pojemnosc': 0, 'max_rpm': 0},
            {'nazwa': 'Hełm typu MICH 2000', 'image_url': 'https://pixnio.com/free-images/2017/02/22/2017-02-22-19-11-09-1200x800.jpg', 'cena': 220, 'waga': 1.6, 'pojemnosc': 0, 'max_rpm': 0},
            {'nazwa': 'Pokrowiec na hełm w kamuflażu', 'image_url': 'https://images.pexels.com/photos/12316900/pexels-photo-12316900.jpeg', 'cena': 50, 'waga': 0.2, 'pojemnosc': 0, 'max_rpm': 0}
        ],
        'Ochrona twarzy i oczu': [
            {'nazwa': 'Gogle balistyczne', 'image_url': 'https://pixnio.com/free-images/2017/02/22/2017-02-22-19-12-00-1200x800.jpg', 'cena': 150, 'waga': 0.3, 'pojemnosc': 0, 'max_rpm': 0},
            {'nazwa': 'Okulary ochronne', 'image_url': 'https://images.pexels.com/photos/4006152/pexels-photo-4006152.jpeg', 'cena': 80, 'waga': 0.1, 'pojemnosc': 0, 'max_rpm': 0},
            {'nazwa': 'Maska stalowa typu Stalker', 'image_url': 'https://pixnio.com/free-images/2017/02/22/2017-02-22-19-12-58-1200x800.jpg', 'cena': 60, 'waga': 0.2, 'pojemnosc': 0, 'max_rpm': 0}
        ],
        'Umundurowanie': [
            {'nazwa': 'Spodnie bojówki', 'image_url': 'https://cdn.pixabay.com/photo/2014/11/24/09/27/camouflage-543668_1280.jpg', 'cena': 250, 'waga': 0.8, 'pojemnosc': 0, 'max_rpm': 0},
            {'nazwa': 'Bluza mundurowa', 'image_url': 'https://cdn.pixabay.com/photo/2015/09/09/16/09/camouflage-931131_1280.jpg', 'cena': 220, 'waga': 0.9, 'pojemnosc': 0, 'max_rpm': 0},
            {'nazwa': 'Koszulka termoaktywna', 'image_url': 'https://images.pexels.com/photos/1344690/pexels-photo-1344690.jpeg', 'cena': 90, 'waga': 0.3, 'pojemnosc': 0, 'max_rpm': 0}
        ],
        'Obuwie': [
            {'nazwa': 'Buty taktyczne wysokie', 'image_url': 'https://images.pexels.com/photos/6682772/pexels-photo-6682772.jpeg', 'cena': 450, 'waga': 1.8, 'pojemnosc': 0, 'max_rpm': 0},
            {'nazwa': 'Buty trekkingowe niskie', 'image_url': 'https://images.pexels.com/photos/4850785/pexels-photo-4850785.jpeg', 'cena': 350, 'waga': 1.2, 'pojemnosc': 0, 'max_rpm': 0},
            {'nazwa': 'Ochraniacze na buty (stuptuty)', 'image_url': 'https://pixnio.com/free-images/2017/02/22/2017-02-22-19-13-14-1200x800.jpg', 'cena': 70, 'waga': 0.4, 'pojemnosc': 0, 'max_rpm': 0}
        ],
        'Plecaki': [
            {'nazwa': 'Plecak taktyczny 25L', 'image_url': 'https://images.pexels.com/photos/1118671/pexels-photo-1118671.jpeg', 'cena': 180, 'waga': 1.2, 'pojemnosc': 25, 'max_rpm': 0},
            {'nazwa': 'Plecak szturmowy 40L', 'image_url': 'https://pixnio.com/free-images/2017/02/22/2017-02-22-19-11-20-1200x800.jpg', 'cena': 280, 'waga': 1.9, 'pojemnosc': 40, 'max_rpm': 0},
            {'nazwa': 'Torba zrzutowa na magazynki', 'image_url': 'https://images.pexels.com/photos/1099616/pexels-photo-1099616.jpeg', 'cena': 50, 'waga': 0.3, 'pojemnosc': 5, 'max_rpm': 0}
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
        "laczna_cena": sum(item.get('cena', 0) for item in ekwipunek),
        "ilosc_przedmiotow": len(ekwipunek) if ekwipunek else 0
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

@app.route('/przymierzanie')
def strona_przymierzanie():
    """Wyświetla stronę przymierzania."""
    kontekst = _pobierz_kontekst_dla_szablonu()
    return render_template('przymierzanie.html', **kontekst)

@app.route('/random')
def strona_random():
    """Wyświetla stronę random."""
    kontekst = _pobierz_kontekst_dla_szablonu()
    return render_template('random.html', **kontekst)

























# --- AKCJE (Dodawanie/Usuwanie) ---

@app.route('/dodaj', methods=['POST'])
def dodaj_przedmiot():
    """Dodaje przedmiot do ekwipunku w sesji."""
    nazwa_przedmiotu = request.form.get('nazwa_przedmiotu')
    przedmiot_do_dodania = WSZYSTKIE_PRZEDMIOTY_LOOKUP.get(nazwa_przedmiotu)
    flash(f'{nazwa_przedmiotu} został dodany do ekwipunku.')

    
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
    nazwa_przedmiotu = request.form.get('nazwa_przedmiotu')
    flash(f'{nazwa_przedmiotu} został usunięty z ekwipunku.')
    if 'ekwipunek' in session and index_do_usuniecia_str is not None:
        try:
            index = int(index_do_usuniecia_str)
            if 0 <= index < len(session['ekwipunek']):
                session['ekwipunek'].pop(index)
                session.modified = True
        except (ValueError, IndexError):
            pass # Ignorujemy błędne żądania
            
    return redirect(request.referrer or url_for('strona_glowna'))

@app.route('/wyczysc', methods=['POST'])
def wyczysc_ekwipunek():
    """Czyści cały ekwipunek."""
    session['ekwipunek'] = []
    session.modified = True
    flash('Ekwipunek został wyczyszczony.')
    return redirect(request.referrer or url_for('strona_glowna'))

if __name__ == '__main__':
    app.run(debug=True)