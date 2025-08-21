from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def strona_glowna():
    karabiny = ["M4A1", "AK-74", "G36"]
    pistolety = ["Glock 17", "Beretta M9", "Desert Eagle"]
    snajperki = ["AWM", "Barrett M82", "SVD Dragunov"]
    return render_template(
        'index.html', 
        lista_karabinow=karabiny,
        lista_pistoletow=pistolety,
        lista_snajperek=snajperki
    )


if __name__ == '__main__':
  app.run(debug=True)